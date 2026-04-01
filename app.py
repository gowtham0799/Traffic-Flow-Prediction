import streamlit as st
import pickle
import pandas as pd

# Load model and columns
model = pickle.load(open("model/model.pkl", "rb"))
columns = pickle.load(open("model/columns.pkl", "rb"))

st.title("🚦 Smart Traffic Prediction System")

st.write("Predict traffic and get smart suggestions for traffic management")

# Inputs
temp = st.number_input("🌡️ Temperature")
hour = st.slider("⏰ Hour", 0, 23)
day = st.slider("📅 Day (0=Mon, 6=Sun)", 0, 6)

if st.button("Predict Traffic"):

    # Create input dataframe
    input_data = pd.DataFrame(columns=columns)
    input_data.loc[0] = 0

    # Fill values
    if 'temperature' in input_data:
        input_data['temperature'] = temp
    if 'hour' in input_data:
        input_data['hour'] = hour
    if 'day' in input_data:
        input_data['day'] = day

    try:
        prediction = model.predict(input_data)
        traffic = int(prediction[0])

        st.success(f"🚗 Predicted Traffic Count: {traffic}")

        # 🚦 CASE STUDY BASED LOGIC
        st.subheader("📊 Traffic Analysis & Smart Suggestions")

        if traffic < 50:
            st.info("🟢 Low Traffic")
            st.write("✔ Smooth traffic flow")
            st.write("✔ No signal changes required")

        elif 50 <= traffic < 100:
            st.warning("🟡 Moderate Traffic")
            st.write("✔ Slight congestion detected")
            st.write("➡️ Suggest optimizing signal timing")

        else:
            st.error("🔴 High Traffic Detected")
            st.write("❗ Heavy congestion likely")
            st.write("➡️ Increase green signal duration")
            st.write("➡️ Suggest alternate routes to drivers")
            st.write("➡️ Enable traffic control measures")

    except Exception as e:
        st.error(f"Error: {e}")