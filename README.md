**Intelligent Email Processing & Automated Customer Response System**

**Task – 1001**  
**Date:** 16-05-2026  

An AI-powered intelligent automation system that processes customer banking emails using **Agentic AI architecture**, Llama 3.2, and Python.


**Problem Statement**

A financial institution receives customer emails regarding:
- Account balance enquiries
- Credit card usage / transaction enquiries
- Account statement requests
- Multiple requests in a single email


This project automates the entire process using **Agentic AI**.

**Features Implemented**

- **Multi-intent detection** in a single email (Scenario 4)
- **Entity extraction** (account number, card number, transaction count, period)
- **Sentiment analysis** (neutral, positive, negative, urgent)
- **Data validation** using mock core banking APIs
- **Smart API decision engine** – calls only required APIs
- **Partial failure handling** (Scenario 5) – returns successful results + polite error for invalid data
- **Professional response email generation** (matches PDF sample)
- **Audit logging** for all steps
- **Clean, modular, production-ready architecture**


**Technology Stack**

- **Language**: Python
- **LLM**: Llama 3.2 (via Ollama – local & private)
- **Agent Framework**: CrewAI
- **Structured Output**: Pydantic + LangChain
- **Mock APIs**: Custom Python functions with in-memory database
- **Architecture**: Agentic AI with specialized agents


intelligent-email-automation/
│
├── agents/                    # AI Agents
│   ├── email_understanding_agent.py
│   └── validation_agent.py
├── apis/                      # Mock Core Banking APIs
│   └── mock_apis.py
├── models/                    # Data schemas (Pydantic)
│   └── schemas.py
├── prompts/                   # LLM Prompts
│   └── intent_prompt.py
├── workflows/                 # Main orchestration logic
│   └── banking_workflow.py
├── utils/                     # Helper functions & logging
│   └── helpers.py
├── tests/                     # Test cases
│   └── test_scenarios.py
├── config/                    # Configuration
│   └── settings.py
├── logs/                      # Audit logs
│   └── app.log
├── app.py                    
├── main.py                    
├── requirements.txt
└── README.md

**How to Run the Project**

**1. Prerequisites**
1. Install **Ollama** from https://ollama.com
2. Pull the model:
   ```bash
   ollama pull llama3.2
Setup
** 1. Create virtual environment **
**2. Activate it**
venv\Scripts\activate     

**3. Install dependencies**
pip install -r requirements.txt
Run the System
python main.py  # for all 5 test cases
pytest tests/ -v # for testing cases
python -m uvicorn app:app --reload --port 8000  # for FastAPI


**Test Results**
The system correctly handles:

Scenario 1 - Balance enquiry 
Scenario 2 - Credit card transactions
Scenario 3 - Statement Request
Scenario 4 - Multiple requests in one email (both balance + card)
Scenario 5 - Partial failure (valid account + invalid card)


**Key Achievements**

Full Agentic AI design with specialized agents - HDFC Sahayak
Structured output using Pydantic 
Smart validation and partial failure handling
Clean, modular, extensible code
Complete folder structure as specified in the task
Logging for auditability


**Assumptions**

Core banking APIs are mocked
No real customer data is used
Email content is provided as plain text
Authentication is simplified


Author: Pradyumna Kapure    
Project Completed: 18 May 2026
