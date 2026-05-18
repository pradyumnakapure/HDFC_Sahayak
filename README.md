# Intelligent Email Processing & Automated Customer Response System

**Task – 1001**  
**Date:** 16-05-2026

HDFC Sahayak - An Banking Email Automation Agent built using **Agentic AI architecture**, **Llama 3.2**, **CrewAI**, and **Python**.

---

# Problem Statement

A financial institution receives customer emails related to:

- Account balance enquiries
- Credit card transaction enquiries
- Account statement requests
- Multiple requests within a single email

---

# Features Implemented

### Multi-Intent Detection
Supports multiple requests within a single customer email.

**Example:**

- Account balance enquiry
- Credit card transaction request
- Statement request
- Combined requests in one email

---

### Entity Extraction

Extracts important banking entities such as:

- Account Number
- Card Number
- Transaction Count
- Time Period

---

### Sentiment Analysis

Detects customer tone:

- Neutral
- Positive
- Negative
- Urgent

---

### Smart API Decision Engine

Calls **only the required banking APIs** based on detected intent.

---

### Data Validation

Validates customer information using **mock core banking APIs**.

---

### Partial Failure Handling

Supports graceful error handling.

If one request succeeds and another fails:

- Returns successful results
- Adds polite failure messaging for invalid inputs

---

### Professional Response Generation

Generates professional banking response emails matching the provided specification.

---

### Audit Logging

Logs:

- Input processing
- Intent detection
- API calls
- Validation
- Final responses

---

### Production-Ready Architecture

- Modular design
- Scalable workflow engine
- Specialized AI agents
- Clean separation of concerns

---

# Technology Stack

| Component | Technology |
|------------|-------------|
| Language | Python |
| LLM | Llama 3.2 (Ollama) |
| Agent Framework | CrewAI |
| Structured Output | Pydantic + LangChain |
| APIs | Mock Core Banking APIs |
| Backend | FastAPI |
| Logging | Python Logging |
| Architecture | Agentic AI |

---

# Project Structure

```bash
intelligent-email-automation/
│
├── agents/
│   ├── email_understanding_agent.py
│   └── validation_agent.py
│
├── apis/
│   └── mock_apis.py
│
├── models/
│   └── schemas.py
│
├── prompts/
│   └── intent_prompt.py
│
├── workflows/
│   └── banking_workflow.py
│
├── utils/
│   └── helpers.py
│
├── tests/
│   └── test_scenarios.py
│
├── config/
│   └── settings.py
│
├── logs/
│   └── app.log
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

---

# System Architecture

```text
Customer Email
      │
      ▼
Email Understanding Agent
(Intent + Entities + Sentiment)
      │
      ▼
Validation Agent
(Data Verification)
      │
      ▼
Workflow Orchestrator
(Intent Routing)
      │
      ▼
Mock Banking APIs
(Account / Card / Statements)
      │
      ▼
Response Generator
      │
      ▼
Final Customer Email
```

---

# Setup Instructions

## 1. Prerequisites

Install **Ollama**:

https://ollama.com

Pull the required model:

```bash
ollama pull llama3.2
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

### Linux / macOS

```bash
python3 -m venv venv
```

---

## 3. Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Project

## Run Main Workflow

Executes all test scenarios.

```bash
python main.py
```

---

## Run Test Cases

```bash
pytest tests/ -v
```

---

## Run FastAPI Server

```bash
python -m uvicorn app:app --reload --port 8000
```

API available at:

```text
http://127.0.0.1:8000/docs
```

---

# Test Scenarios Covered

| Scenario | Status |
|-----------|---------|
| Balance Enquiry | Yes |
| Credit Card Transactions | Yes |
| Statement Request | Yes |
| Multi-Intent Email | Yes |
| Partial Failure Handling | Yes |

---

## Scenario 1 Balance Enquiry

Customer requests account balance.

**Result:**  
Intent detected -> account validated -> balance API called -> response generated.

---

## Scenario 2 Credit Card Transactions

Customer requests recent card transactions.

**Result:**  
Card validated -> transaction API called -> response generated.

---

## Scenario 3 Statement Request

Customer requests account statement.

**Result:**  
Statement workflow executed successfully.

---

## Scenario 4 Multiple Requests

Single email containing:

- Balance enquiry
- Card transaction request

**Result:**  
Multiple intents detected and processed independently.

---

## Scenario 5 Partial Failure

Input contains:

- Valid account
- Invalid card

**Result:**  

- Balance request succeeds
- Card request fails gracefully
- Combined professional response returned

---

# Key Achievements

- Full Agentic AI design with specialized agents

- Multi-intent email processing

- Structured outputs using Pydantic

- Smart API routing

- Validation layer

- Partial failure handling

- Professional email generation

- Logging and auditability

- Clean modular architecture

---

# Assumptions

- Core banking APIs are mocked.
- No real customer data is used.
- Email content is provided as plain text.
- Authentication is simplified for demonstration purposes.

---

# Future Improvements

Potential enhancements:

- Real banking API integration
- Authentication & authorization
- Database persistence
- Email server integration
- Vector memory for conversation history
- Docker deployment
- Kubernetes orchestration
- Monitoring dashboard

---

# Author

**Pradyumna Kapure**

Project Completed: **18 May 2026**

---
