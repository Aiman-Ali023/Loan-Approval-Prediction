import streamlit as st
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(page_title="Loan Approval Predictor", page_icon="🏦", layout="centered")

st.title("🏦 Loan Approval Prediction System")
st.write("Enter the applicant's details below to get a real-time prediction and probability score.")

# --- Sidebar / Input Section ---
st.header("Applicant Information")

col1, col2 = st.columns(2)

with col1:
    applicant_income = st.number_input("Applicant Monthly Income ($)", min_value=0, value=5000, step=500)
    coapplicant_income = st.number_input("Co-Applicant Monthly Income ($)", min_value=0, value=1500, step=500)
    loan_amount = st.number_input("Loan Amount Requested ($)", min_value=0, value=150000, step=5000)
    loan_term = st.selectbox("Loan Term (Months)", [120, 180, 240, 360], index=3)

with col2:
    credit_score = st.slider("Credit Score (CICO)", min_value=300, max_value=850, value=710)
    dependents = st.selectbox("Number of Dependents", [0, 1, 2, "3+"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Preprocessing / Model Logic
def predict_loan_approval(income, co_income, loan, term, credit, deps, edu, area):
    # Rule-based model mock for prediction (Replace with `joblib.load('model.pkl')`)
    total_income = income + co_income
    debt_to_income_ratio = loan / (total_income * 12 + 1e-5)
    
    base_prob = 0.5
    
    # Adjust probability based on features
    if credit >= 700:
        base_prob += 0.3
    elif credit < 600:
        base_prob -= 0.3
        
    if debt_to_income_ratio < 3.0:
        base_prob += 0.15
    else:
        base_prob -= 0.2
        
    if edu == "Graduate":
        base_prob += 0.05
        
    # Bound probability between 0 and 1
    probability = max(0.05, min(0.98, base_prob))
    prediction = "Approved" if probability >= 0.50 else "Rejected"
    
    return prediction, probability

# --- Prediction Action ---
if st.button("Predict Loan Status"):
    prediction, probability = predict_loan_approval(
        applicant_income, coapplicant_income, loan_amount, loan_term, credit_score, dependents, education, property_area
    )
    
    st.divider()
    st.subheader("Prediction Results")
    
    # Display Result Card
    if prediction == "Approved":
        st.success(f"**Status:** {prediction} 🎉")
    else:
        st.error(f"**Status:** {prediction} ❌")
        
    st.metric(label="Approval Probability Score", value=f"{probability * 100:.1f}%")
    st.progress(float(probability))

# --- Preset Test Cases for Quick Submission Screenshots ---
st.divider()
st.subheader("🧪 Test Cases for Proof Submission")

test_case = st.radio("Load Sample Test Case:", ["None", "Test Case 1 (High Quality - Approved)", "Test Case 2 (High Risk - Rejected)"])

if test_case == "Test Case 1 (High Quality - Approved)":
    st.info("Inputs: High Income ($8,000), Strong Credit Score (760), Low Loan-to-Income ratio.")
elif test_case == "Test Case 2 (High Risk - Rejected)":
    st.info("Inputs: Low Income ($1,800), Poor Credit Score (520), High Loan Request ($300,000).")