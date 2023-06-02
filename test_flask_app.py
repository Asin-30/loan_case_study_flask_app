import pytest

from app import app

## we need to run a server to test the flask app
# using pytest fixtures : allows to write piece of code that are reusable across tests 
# hence i'll be allowed to test various funcion of loan.py with one single server.

# this will be running server and will take all the requests made (/ping endpoint in loan.py)

# server
@pytest.fixture
def client(): 
    return app.test_client()


# testing the ping end point
def test_ping(client):
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.json == {'Message': 'This end point is working !!'}


# testing the 'predict' endpoint
def test_prediction(client):
    test_data = {"Gender": "Male","Married": "married","applicant_income": 50000, "loan_amount": 1000000,"credit_history": "Uncleared Debts"}
    response = client.post('/predict', json = test_data)
    assert response.status_code == 200
    assert response.json == {"loan_approval_status": "Approved"}