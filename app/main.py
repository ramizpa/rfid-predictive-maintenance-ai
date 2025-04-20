import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")

st.title("🔧 RFID Predictive Maintenance AI")

uploaded_file = st.file_uploader("Upload RFID Data CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
    X = df[['rssi', 'temperature', 'voltage', 'read_rate', 'uptime', 'hour']]
    predictions = model.predict(X)
    df['prediction'] = ["Failing Soon" if p == 1 else "Healthy" for p in predictions]
    st.write(df)
    st.success("Prediction Complete!")
