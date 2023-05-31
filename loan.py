from flask import Flask, request
import pickle

# intializing app
app = Flask(__name__)



# Loading the ML model
model_pkl = open('./artefacts/classifier.pkl','rb') # reading model
clf = pickle.load(model_pkl)

# ENDPOINT DEVELOPMENT 

# to attach it the BASE URL, we use decorators ('@'). 
# And for that URL to point toward the desired endpoint we put name in it
@app.route('/ping', methods = ['GET'])  # method will be what user is wanting whether it is get or post / what request type is app recieving.
def ping():
    return {'Message': 'This end point is working !!'}



## creating endpoint to get a template of the request for model inference
@app.route('/template', methods = ['GET'])
def temp():
    return {
        "Gender": "Male/Female",
        "Married": "Married/Unmarried",
        "applicant_income": "<Numeric salary>",
        "loan_amount": "Numeric loan amount",
        "credit_history": "Cleared Debts/Uncleared Debts"
    }   


# creating an endpoint for classification
@app.route('/predict', methods = ['GET','POST'])
def prediction():
    '''
    return the prediction after user enters the data.
    The data user enters is stored in json format
    and flask's request is used to read it.
    '''
    # to read the user's request data that is stored in json format
    loan_req = request.get_json()


    if loan_req['Gender'] == "Male":
        gender = 0
    else:
        gender = 1

    if loan_req['Married'] == "Unmarried":
        marital_status = 0
    else:
        marital_status = 1

    if loan_req['credit_history'] == "Unclear Debts":
        credit_status = 0
    else:
        credit_status = 1
    
    applicant_income = loan_req['applicant_income']
    loan_amt = loan_req['loan_amount']

    result = clf.predict([[gender, marital_status, applicant_income, loan_amt, credit_status]])

    if result == 0:
        pred = "Rejected"
    else: 
        pred = "Approved"

    return {"loan_approval_status": pred} # storing the loan_approval prediction data in the dataset


if __name__ == '__main__':
    loan.run()