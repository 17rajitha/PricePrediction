import streamlit as st
import pickle
import numpy as np

# Load the trained ML model
with open("insurance_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("💰 Insurance Premium Calculator")

# User input fields
age = st.number_input("Enter Age", min_value=18, max_value=100, value=30)
diabetes = st.selectbox("Do you have diabetes?", ["No", "Yes"])
blood_pressure = st.selectbox("Do you have blood pressure problems?", ["No", "Yes"])
transplants = st.selectbox("Have you had any organ transplants?", ["No", "Yes"])
chronic_diseases = st.selectbox("Do you have any chronic diseases?", ["No", "Yes"])
weight = st.number_input("Enter your weight (kg)", min_value=30, max_value=200, value=70)
allergies = st.selectbox("Do you have known allergies?", ["No", "Yes"])
cancer_history = st.selectbox("Any family history of cancer?", ["No", "Yes"])
surgeries = st.number_input("Number of major surgeries", min_value=0, max_value=10, value=0)

# Convert categorical inputs to numerical
diabetes = 1 if diabetes == "Yes" else 0
blood_pressure = 1 if blood_pressure == "Yes" else 0
transplants = 1 if transplants == "Yes" else 0
chronic_diseases = 1 if chronic_diseases == "Yes" else 0
allergies = 1 if allergies == "Yes" else 0
cancer_history = 1 if cancer_history == "Yes" else 0

# Feature Engineering (if needed)
age_chronic = age * chronic_diseases
diabetes_bp = diabetes * blood_pressure

# Create input array
features = np.array([[age, diabetes, blood_pressure, transplants, chronic_diseases, weight,
                      allergies, cancer_history, surgeries, age_chronic, diabetes_bp]])

# Predict insurance premium
if st.button("Calculate Premium"):
    premium = model.predict(features)[0]
    st.success(f"💰 Estimated Insurance Premium: ₹{round(premium, 2)}")

