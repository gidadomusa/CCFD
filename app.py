import streamlit as st
import pandas as pd
import numpy as np
import joblib
import datetime
import sqlite3

st.header("Credit Card Fraud Detection")

with st.form("Credit_Card_Details"):
    st.write("Please enter the details of the transaction below:")

    user_input_time = st.number_input("Time", min_value=0)

    user_input_v1 = st.number_input("V1")
    user_input_v2 = st.number_input("V2")
    user_input_v3 = st.number_input("V3")
    user_input_v4 = st.number_input("V4")
    user_input_v5 = st.number_input("V5")
    user_input_v6 = st.number_input("V6")
    user_input_v7 = st.number_input("V7")
    user_input_v8 = st.number_input("V8")
    user_input_v9 = st.number_input("V9")
    user_input_v10 = st.number_input("V10")
    user_input_v11 = st.number_input("V11")
    user_input_v12 = st.number_input("V12")
    user_input_v13 = st.number_input("V13")
    user_input_v14 = st.number_input("V14")
    user_input_v15 = st.number_input("V15")  
    user_input_v16 = st.number_input("V16")
    user_input_v17 = st.number_input("V17")
    user_input_v18 = st.number_input("V18")
    user_input_v19 = st.number_input("V19")
    user_input_v20 = st.number_input("V20")
    user_input_v21 = st.number_input("V21")
    user_input_v22 = st.number_input("V22")
    user_input_v23 = st.number_input("V23")
    user_input_v24 = st.number_input("V24")
    user_input_v25 = st.number_input("V25")
    user_input_v26 = st.number_input("V26")
    user_input_v27 = st.number_input("V27")
    user_input_v28 = st.number_input("V28")
    user_input_amount = st.number_input("Amount", min_value=0.0)


    # Submit button inside the form
    submitted = st.form_submit_button("Check for fraud")

def prepare_input():
    input_dict = {
        'Time': user_input_time,
        'V1': user_input_v1,
        'V2': user_input_v2,
        'V3': user_input_v3,
        'V4': user_input_v4,
        'V5': user_input_v5,
        'V6': user_input_v6,
        'V7': user_input_v7,
        'V8': user_input_v8,
        'V9': user_input_v9,
        'V10': user_input_v10,
        'V11': user_input_v11,
        'V12': user_input_v12,
        'V13': user_input_v13,
        'V14': user_input_v14,
        'V15': user_input_v15,
        'V16': user_input_v16,
        'V17': user_input_v17,
        'V18': user_input_v18,
        'V19': user_input_v19,
        'V20': user_input_v20,
        'V21': user_input_v21,
        'V22': user_input_v22,
        'V23': user_input_v23,
        'V24': user_input_v24,
        'V25': user_input_v25,
        'V26': user_input_v26,
        'V27': user_input_v27,
        'V28': user_input_v28,
        'Amount': user_input_amount

    }

    return pd.DataFrame([input_dict])

if submitted:
    input_data = prepare_input()

    # Load the model
    model = joblib.load('rf_model.joblib')

    # Make prediction
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error(" The transaction is **fraudulent**.")
    else:
        st.success("The transaction is **legitimate**.")

    # Log transaction to database
    def insert_transaction(time, amount, v_values):
        conn = sqlite3.connect('credit_card.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO cc_transactions (date,V1, V2, V3, V4, V5, V6, V7, V8, V9,amount)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), *v_values, amount))
        conn.commit()
        cursor.close()
        conn.close()

    v_values = [user_input_v1, user_input_v2, user_input_v3, user_input_v4,
                user_input_v5, user_input_v6, user_input_v7, user_input_v8, user_input_v9]
    
    insert_transaction(user_input_time, user_input_amount, v_values)
    st.success("Transaction details logged successfully.")
else:
    st.info("Please fill in the transaction details and click 'Check for fraud'.")
    st.warning("Make sure to fill all fields before submitting.")      
