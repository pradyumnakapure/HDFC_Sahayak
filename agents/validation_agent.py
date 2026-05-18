# I will create a ValidationAgent class that uses CrewAI to validate banking data such as account numbers and credit card numbers.
# This agent will call mock validation APIs (validate_account and validate_card) to check if the provided data is valid. The agent will be designed to handle both types of data and will return clear

from crewai import Agent
from apis.mock_apis import validate_account, validate_card


class ValidationAgent:
    """Validates banking data like account numbers and credit cards."""

    def __init__(self):
        self.agent = Agent(
            role="Banking Data Validation Specialist",
            goal="Validate account numbers and credit card numbers using core banking APIs",
            backstory=(
                "You are a strict and accurate validation officer in a bank. "
                "You always call the correct validation API and clearly report valid/invalid results."
            ),
            llm="ollama/llama3.2",          # ← Fixed: Use string instead of ChatOllama object
            verbose=False,                   # ← Clean output (no big boxes)
            allow_delegation=False,
        )

    def validate(self, account_number: str | None = None, card_number: str | None = None) -> dict:
        """Validate extracted account/card data using mock APIs."""
        results = {}

        if account_number:
            results["account"] = self._safe_validate(validate_account, account_number)

        if card_number:
            results["card"] = self._safe_validate(validate_card, card_number)

        return results

    def _safe_validate(self, validator, value):
        """Run a validation function safely and handle any errors."""
        try:
            return validator(value)
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}
