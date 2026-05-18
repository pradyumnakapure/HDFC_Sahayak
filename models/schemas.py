# This module defines the data schemas for analyzing customer emails in the intelligent email automation system.

from pydantic import BaseModel, Field
from typing import List, Literal, Optional

class Intent(BaseModel):
    intent_type: Literal["balance_enquiry", "card_usage", "statement_request"]
    confidence: float = Field(ge=0.0, le=1.0, default=0.95)

class ExtractedEntities(BaseModel):
    account_number: Optional[str] = None
    card_number: Optional[str] = None
    period: Optional[str] = None          # e.g. "April 2026"
    transaction_count: int = 5

class CustomerEmailAnalysis(BaseModel):
    intents: List[Intent]
    sentiment: Literal["neutral", "positive", "negative", "urgent"]
    entities: ExtractedEntities
    summary: str
    customer_name: Optional[str] = None
