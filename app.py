# This is the main application file for the Intelligent Banking Email Automation system. 
# It sets up a FastAPI server with endpoints to process customer emails and perform health checks. 

from fastapi import FastAPI
from pydantic import BaseModel
from workflows.banking_workflow import BankingEmailWorkflow
import uvicorn

app = FastAPI(
    title="Intelligent Banking Email Automation API",
    description="AI-powered system that processes customer banking emails using Agentic AI",
    version="1.0.0"
)

class EmailRequest(BaseModel):
    email_text: str

class EmailResponse(BaseModel):
    status: str
    response_email: str
    analysis_summary: str = None

workflow = BankingEmailWorkflow()

@app.post("/process-email", response_model=EmailResponse)
async def process_email(request: EmailRequest):
    """Process a customer email and return professional response"""
    try:
        final_email = workflow.run(request.email_text)
        return EmailResponse(
            status="success",
            response_email=final_email,
            analysis_summary="Email processed successfully by Agentic AI"
        )
    except Exception as e:
        return EmailResponse(
            status="error",
            response_email=f"Error processing email: {str(e)}"
        )

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "Intelligent Email Automation System is running"}

# For running directly with uvicorn
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
