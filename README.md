<<<<<<< HEAD
# rfid-predictive-maintenance-ai
AI-Enabled Predictive Maintenance System for RFID Readers
=======
# AI-Enabled Predictive Maintenance of RFID Systems

This project demonstrates a machine learning-based approach to predict failures in RFID systems using telemetry data. By leveraging features such as RSSI, temperature, voltage, and read rate, the system forecasts potential failures and enables proactive maintenance.

---

## 🧾 Abstract

This AI-powered system analyzes RFID telemetry data to identify signs of potential hardware or performance failures. The goal is to prevent system downtimes by using predictive maintenance, improving operational efficiency in RFID-enabled environments such as logistics, warehousing, and manufacturing.

---

## 🎯 Objectives

- Simulate and analyze RFID sensor data  
- Train an AI model to predict system failure  
- Deploy a dashboard for real-time predictions and analytics

---

## 📊 Dataset

Synthetic dataset with 10,000 records:
- `timestamp`: Time of record
- `rssi`: Signal strength
- `temperature`: Device internal temperature
- `voltage`: Power voltage level
- `read_rate`: Read success rate
- `uptime`: System uptime in seconds
- `failed`: 1 if failure occurred, else 0

---

## 🧠 Machine Learning

- Random Forest classifier
- Feature analysis and correlation heatmap
- Model evaluation using accuracy, recall, precision
- Exported as `rfid_failure_model.pkl`

---

## 🖥️ Streamlit Dashboard

- Upload new sensor data
- Get real-time failure predictions
- Visual analytics and insights

---

## 🧰 Tech Stack

- Python, Pandas, NumPy, Scikit-learn  
- Matplotlib, Seaborn, Plotly  
- Streamlit

---

## 🚀 Run the App

```bash
pip install -r requirements.txt
streamlit run app/main.py
>>>>>>> ab65cbe (Initial commit - AI Predictive Maintenance for RFID)
