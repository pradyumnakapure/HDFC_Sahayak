from workflows.banking_workflow import BankingEmailWorkflow

def test_scenario_1():
    """Test Scenario 1 - Balance Enquiry"""
    system = BankingEmailWorkflow()
    email = "Please provide my savings account balance for account number 1234567890."
    response = system.run(email)
    
    assert response is not None
    assert "Account Balance" in response
    assert "1234567890" in response
    assert "INR" in response
    print("✅ Test Scenario 1 (Balance Enquiry) Passed")


def test_scenario_2():
    """Test Scenario 2 - Credit Card Usage"""
    system = BankingEmailWorkflow()
    email = "Please share my last 5 credit card transactions for card 4567XXXX8901."
    response = system.run(email)
    
    assert response is not None
    assert "Credit Card Transactions" in response
    assert "4567XXXX8901" in response
    print("✅ Test Scenario 2 (Credit Card Usage) Passed")


def test_scenario_3():
    """Test Scenario 3 - Statement Request"""
    system = BankingEmailWorkflow()
    email = "Kindly send my bank statement for April 2026."
    response = system.run(email)
    
    assert response is not None
    assert "Bank Statement" in response
    assert "April 2026" in response
    assert "Reference" in response
    print("✅ Test Scenario 3 (Statement Request) Passed")


def test_scenario_4():
    """Test Scenario 4 - Multiple Requests in One Email"""
    system = BankingEmailWorkflow()
    email = "Please share my account balance for account 1234567890 and also send last 3 transactions of my credit card 987654321."
    response = system.run(email)
    
    assert response is not None
    assert "Account Balance" in response
    assert "Credit Card Transactions" in response
    assert "1234567890" in response
    assert "987654321" in response
    print("✅ Test Scenario 4 (Multiple Requests) Passed")


def test_scenario_5():
    """Test Scenario 5 - Partial Failure"""
    system = BankingEmailWorkflow()
    email = "Please provide balance for account 1234567890 and card transactions for card 999999999."
    response = system.run(email)
    
    assert response is not None
    assert "Account Balance" in response
    assert "Credit Card Request" in response
    assert "could not be validated" in response
    print("✅ Test Scenario 5 (Partial Failure) Passed")


if __name__ == "__main__":
    test_scenario_1()
    test_scenario_2()
    test_scenario_3()
    test_scenario_4()
    test_scenario_5()
    print("\n🎉 All 5 scenarios tested successfully!")
