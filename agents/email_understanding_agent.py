# I will create an EmailUnderstandingAgent class that uses CrewAI to analyze customer emails.
# This agent will classify the intent, sentiment, extract entities, and summarize the email content. 
# My agent name will be HDFC Sahayak, and it will be trained to understand customer emails related to banking services. 
# The agent will use the INTENT_CLASSIFICATION_PROMPT to guide its analysis and will return a CustomerEmailAnalysis object containing the results.

from crewai import Agent, Crew, Task 
from models.schemas import CustomerEmailAnalysis
from prompts.intent_prompt import INTENT_CLASSIFICATION_PROMPT


class EmailUnderstandingAgent:
    def __init__(self):
        self.agent = Agent(
            role="HDFC Sahayak",                                      # ← Updated Name
            goal="Act as HDFC Sahayak - an intelligent AI assistant that perfectly understands customer banking emails and provides fast, accurate responses.",
            backstory="""You are HDFC Sahayak, HDFC Bank's intelligent AI email assistant.
You have deep knowledge of banking products, excellent customer service skills, and you always respond professionally and helpfully.""",
            llm="ollama/llama3.2",
            verbose=False,
            allow_delegation=False
        )

    def analyze(self, email: str) -> CustomerEmailAnalysis:
        """Main method that analyzes one customer email"""
        task = Task(
            description=INTENT_CLASSIFICATION_PROMPT.format(
                email=email,
                CustomerEmailAnalysis=CustomerEmailAnalysis.model_json_schema()
            ),
            expected_output="A complete CustomerEmailAnalysis object with intents, sentiment, entities and summary",
            agent=self.agent,
            output_pydantic=CustomerEmailAnalysis
        )

        crew = Crew(
            agents=[self.agent],
            tasks=[task],
            verbose=False
        )

        result = crew.kickoff()
        return CustomerEmailAnalysis.model_validate_json(result.raw)
