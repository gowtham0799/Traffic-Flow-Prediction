import streamlit as st
import pickle
import pandas as pd

# Load model and columns
model = pickle.load(open("model/model.pkl", "rb"))
columns = pickle.load(open("model/columns.pkl", "rb"))

st.title("🚦 Traffic Prediction")

temp = st.number_input("Temperature")
hour = st.slider("Hour", 0, 23)
day = st.slider("Day", 0, 6)

if st.button("Predict"):

    # Create empty dataframe with all columns
    input_data = pd.DataFrame(columns=columns)
    input_data.loc[0] = 0

    # Fill required values
    if 'temperature' in input_data:
        input_data['temperature'] = temp
    if 'hour' in input_data:
        input_data['hour'] = hour
    if 'day' in input_data:
        input_data['day'] = day

    try:
        prediction = model.predict(input_data)
        st.success(f"🚗 Traffic Count: {int(prediction[0])}")
    except Exception as e:
        st.error(f"Error: {e}")