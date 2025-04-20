import streamlit as st
import joblib
import os

st.set_page_config(page_title="RFID Model Viewer", layout="centered")
st.title("📦 RFID Predictive Maintenance - Model Viewer")

# Construct the correct path to the model
current_dir = os.path.dirname(__file__)
model_path = os.path.abspath(os.path.join(current_dir, "..", "models", "rfid_failure_model.pkl"))

# Load the model
try:
    model = joblib.load(model_path)
    st.success("✅ Model loaded successfully!")
    st.subheader("🔍 Model Info")
    st.code(str(model), language="python")
except FileNotFoundError:
    st.error(f"❌ Model file not found at: {model_path}")

