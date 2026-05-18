# This module contains mock APIs for simulating banking operations such as fetching account balances, card transactions, and generating statements.

from pydantic import BaseModel
from typing import List
import random
from datetime import datetime

class AccountBalance(BaseModel):
    account_number: str
    balance: float
    currency: str = "INR"
    customer_name: str

class Transaction(BaseModel):
    date: str
    description: str
    amount: float
    type: str

class CardTransactions(BaseModel):
    card_number: str
    transactions: List[Transaction]

class Statement(BaseModel):
    period: str
    message: str
    reference: str

# In-memory fake database
MOCK_ACCOUNTS = {
    "1234567890": {"name": "John Doe", "balance": 125000.75},
    "9876543210": {"name": "Jane Smith", "balance": 45600.0},
}

MOCK_CARDS = {
    "4567XXXX8901": True,
    "987654321": True,
}

def get_account_balance(account_number: str):
    if account_number not in MOCK_ACCOUNTS:
        raise ValueError("Invalid account number")
    data = MOCK_ACCOUNTS[account_number]
    return AccountBalance(
        account_number=account_number,
        balance=data["balance"],
        customer_name=data["name"]
    ).model_dump()

def get_card_transactions(card_number: str, count: int = 5):
    if card_number not in MOCK_CARDS:
        raise ValueError("Invalid card number")
    txs = []
    for i in range(count):
        txs.append(Transaction(
            date=datetime.now().strftime("%Y-%m-%d"),
            description=f"Transaction {i+1}",
            amount=round(random.uniform(100, 5000), 2),
            type=random.choice(["CREDIT", "DEBIT"])
        ).model_dump())
    return CardTransactions(card_number=card_number, transactions=txs).model_dump()

def get_statement(period: str):
    """GetStatementAPI - Mock"""
    return Statement(
        period=period,
        message=f"Statement for {period} generated successfully.",
        reference=f"STAT-{period.replace(' ', '-')}-{random.randint(10000,99999)}"
    ).model_dump()

def validate_account(account_number: str):
    if account_number in MOCK_ACCOUNTS:
        return {"status": "VALID", "customer_name": MOCK_ACCOUNTS[account_number]["name"]}
    return {"status": "INVALID"}

def validate_card(card_number: str):
    return {"status": "VALID" if card_number in MOCK_CARDS else "INVALID"}
