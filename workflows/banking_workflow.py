from agents.email_understanding_agent import EmailUnderstandingAgent
from agents.validation_agent import ValidationAgent
from apis.mock_apis import get_account_balance, get_card_transactions, get_statement
from utils.helpers import setup_logging
import logging

logger = setup_logging()


class BankingEmailWorkflow:
    def __init__(self):
        self.understanding_agent = EmailUnderstandingAgent()
        self.validation_agent = ValidationAgent()
        logger.info("BankingEmailWorkflow initialized")

    def run(self, email_text: str) -> str:
        analysis = self.understanding_agent.analyze(email_text)

        validation_result = self.validation_agent.validate(
            account_number=analysis.entities.account_number,
            card_number=analysis.entities.card_number,
        )

        api_responses = {}

        for intent in analysis.intents:
            if intent.intent_type == "balance_enquiry" and analysis.entities.account_number:
                if validation_result.get("account", {}).get("status") == "VALID":
                    api_responses["balance"] = self._get_balance(analysis.entities.account_number)

            if intent.intent_type == "card_usage" and analysis.entities.card_number:
                if validation_result.get("card", {}).get("status") == "VALID":
                    count = analysis.entities.transaction_count   # Direct access - no default
                    api_responses["transactions"] = self._get_card_transactions(
                        analysis.entities.card_number, count=count
                    )
                else:
                    logger.warning("Skipped card API - invalid card number")

            if intent.intent_type == "statement_request" and analysis.entities.period:
                api_responses["statement"] = self._get_statement(analysis.entities.period)

        return self._generate_response(analysis, validation_result, api_responses)

    def _get_balance(self, account_number: str) -> dict:
        try:
            return get_account_balance(account_number)
        except Exception as e:
            logger.error(f"Balance API error: {e}")
            return {}

    def _get_card_transactions(self, card_number: str, count: int = 5) -> dict:
        try:
            return get_card_transactions(card_number, count=count)
        except Exception as e:
            logger.error(f"Card API error: {e}")
            return {}

    def _get_statement(self, period: str) -> dict:
        try:
            return get_statement(period)
        except Exception as e:
            logger.error(f"Statement API error: {e}")
            return {}

    def _generate_response(self, analysis, validation_result, api_responses):
        lines = ["Dear Customer,", "", "We have processed your request successfully.", ""]

        if balance := api_responses.get("balance"):
            lines.extend([
                "**Account Balance:**",
                f"• Account Number: {balance.get('account_number', 'XXXXXX')}",
                f"• Available Balance: INR {balance.get('balance', 0):,.2f}",
                "",
            ])

        if tx_data := api_responses.get("transactions"):
            count = analysis.entities.transaction_count
            lines.extend([
                "**Credit Card Transactions:**",
                f"Card Number: {tx_data['card_number']}",
                f"Showing last {count} transactions:",      # This must use the extracted count
                "",
            ])
            for tx in tx_data["transactions"]:
                lines.append(f"• {tx['date']} | {tx['description']} | {tx['type']} | INR {tx['amount']:,.2f}")
            lines.append("")

        if stmt := api_responses.get("statement"):
            lines.extend([
                "**Bank Statement:**",
                f"• Period: {stmt.get('period')}",
                f"• Reference: {stmt.get('reference')}",
                "• Your statement has been generated and is ready for download.",
                "",
            ])

        if validation_result.get("account", {}).get("status") == "INVALID":
            lines.extend(["**Account Request:**", "The account number provided could not be validated.", "Kindly recheck the account details and resend your request.", ""])

        if validation_result.get("card", {}).get("status") == "INVALID":
            lines.extend(["**Credit Card Request:**", "The credit card number provided could not be validated.", "Kindly recheck the card details and resend your request.", ""])

        lines.extend(["", "Thank you,", "Customer Support Team"])
        return "\n".join(lines)
