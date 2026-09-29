# 🏦 Loan Approval Prediction System

An end-to-end Machine Learning pipeline and interactive Streamlit web application designed to automate credit risk assessment and predict loan eligibility for applicants based on financial and demographic indicators.

---

## 📌 Problem Statement
Financial institutions evaluate loan requests based on creditworthiness and financial stability. Manual evaluations can be time-consuming and prone to human error. This project implements a binary classification model that predicts whether a loan application will be **Approved (`1`)** or **Rejected (`0`)**, enabling fast and standardized risk assessment.

---

## 📁 Dataset & Features
The dataset comprises applicant financial records with 12 initial feature dimensions:

* **`ApplicantIncome`**: Principal applicant's monthly earnings ($).
* **`CoapplicantIncome`**: Secondary household earnings ($).
* **`LoanAmount`**: Total requested principal amount ($ thousands).
* **`Loan_Amount_Term`**: Tenure for repayment (in months).
* **`Credit_History`**: Credit guidelines compliance score (`1` = Meets guidelines, `0` = Does not meet).
* **`Gender`, `Married`, `Dependents`, `Education`, `Self_Employed`, `Property_Area`**: Demographic indicators.
* **`Loan_Status`**: Target variable (`Y` = Approved, `N` = Rejected).

---

## 🧹 Data Preprocessing Stratergy
1. **Missing Value Imputation:**
   * **Categorical variables** (`Gender`, `Married`, `Dependents`, `Self_Employed`, `Credit_History`) were imputed using Mode values.
   * **Numerical variables** (`LoanAmount`, `Loan_Amount_Term`) were imputed using Median values to avoid skewness from extreme outliers.
2. **Feature Engineering & Transformation:**
   * Removed non-predictive keys (`Loan_ID`).
   * Transformed categorical parameters into numerical matrices via `LabelEncoder`.

---

## ⚙️ Model & Evaluation Results
A **Logistic Regression** classifier was trained on an 80/20 train/test split.

### Key Performance Metrics
* **Accuracy:** `78.86%`
* **ROC-AUC Score:** `0.7811`
* **Recall (Approved Class):** `98.75%`
* **Precision (Approved Class):** `75.96%`
* **F1-Score:** `0.8587`

### Classification Analysis
The model achieves high sensitivity for detecting approved applicants ($98.75\%$ Recall), serving as a reliable initial automated screening mechanism. Exploratory Data Analysis confirmed that **Credit History** is the primary driver of loan approval decisions.

---

## 🖥️ Streamlit Application Setup

### Prerequisites
Ensure Python 3.8+ is installed on your machine.

### Installation & Local Run
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Loan-Approval-Prediction.git](https://github.com/YOUR_USERNAME/Loan-Approval-Prediction.git)
   cd Loan-Approval-Prediction