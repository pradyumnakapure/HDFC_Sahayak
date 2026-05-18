# This is the main entry point for testing the Intelligent Email Processing System for HDFC Sahayak.


from workflows.banking_workflow import BankingEmailWorkflow

if __name__ == "__main__":
    print("Starting Intelligent Email Processing System...\n")
    
    system = BankingEmailWorkflow()

    tests = {
        "Scenario 1 - Balance Enquiry": 
            "Please provide my savings account balance for account number 1234567890.",
        
        "Scenario 2 - Credit Card Usage": 
            "Please share my last 5 credit card transactions for card 4567XXXX8901.",
        
        "Scenario 3 - Statement Request": 
            "Kindly send my bank statement for April 2026.",
        
        "Scenario 4 - Multiple Requests": 
            "Please share my account balance for account 1234567890 and also send last 3 transactions of my credit card 987654321.",
        
        "Scenario 5 - Partial Failure": 
            "Please provide balance for account 1234567890 and card transactions for card 999999999."
    }

    for name, email in tests.items():
        print("=" * 90)
        print(f"TESTING: {name}")
        print("=" * 90)
        print(f"Command : {email}")
        print("\nHDFC Sahayak is working...\n")
        print("Output:")
        print("-" * 40)
        
        final_email = system.run(email)
        print(final_email)
        
        print("\n" + "=" * 90 + "\n")

    print("All 5 scenarios completed successfully.")
