
import streamlit as st
import pandas as pd
import joblib

# Title of the app
st.title("ICMP Flood Attack Detection")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Load model
model = joblib.load("random_forest_model.pkl")

# Define preprocessing function (modify if you preprocessed differently)
def preprocess(df):
    df = df.select_dtypes(include=['int64', 'float64'])
    return df

# Predict when file is uploaded
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    processed_data = preprocess(data)
    
    try:
        predictions = model.predict(processed_data)
        data['Prediction'] = predictions
        st.write("Prediction Result:")
        st.dataframe(data)
        csv = data.to_csv(index=False).encode()
        st.download_button("Download Result CSV", csv, "prediction_results.csv", "text/csv")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
