from flask import Flask, render_template, request

app = Flask(__name__)

# Loan prediction logic (basic conditions for demonstration)
def predict_loan(gender, marital_status, applicant_income, cibil_score):
    total_income = int(applicant_income) # For simplicity, we assume total income is the same as applicant income

    # Simple conditions for eligibility
    if total_income >= 30000:
        loan_status = "Approved"
        loan_amount = total_income * 0.4  # Example calculation: 40% of total income
    elif total_income >= 20000:
        loan_status = "Approved"
        loan_amount = total_income * 0.3  # Example calculation: 30% of total income
    else:
        loan_status = "Not Approved"
        loan_amount = 0

    return loan_status, loan_amount

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/loan', methods=['POST'])
def loan():
    gender = request.form['gender']
    marital_status = request.form['marital_status']
    applicant_income = request.form['applicant_income']
    cibil_score = request.form['cibil_score']

    # Predict loan eligibility (now called Loan Map)
    result, loan_amount = predict_loan(gender, marital_status, applicant_income, cibil_score)

    return render_template('result.html', result=result, loan_amount=loan_amount)

if __name__ == '__main__':
    app.run(debug=True)