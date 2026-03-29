# 🚦 Traffic Flow Prediction using Machine Learning

## 📌 Project Overview

This project predicts hourly traffic flow using a **Random Forest Regressor** based on historical data. It considers environmental and temporal factors such as temperature, time, weather conditions, and location to estimate traffic volume.

---

## 🎯 Aim

To build a machine learning model that can accurately predict traffic counts and help in better traffic management and planning.

---

## 🧠 Algorithm Used

* Random Forest Regression
* Supervised Machine Learning Algorithm
* Handles non-linear relationships effectively

---

## 📊 Features Used

* 🌡️ Temperature
* ⏰ Hour of the day
* 📅 Day of the week
* 🌦️ Weather conditions
* 📍 Location

---

## ⚙️ Project Workflow

1. Data Collection (Excel dataset)
2. Data Preprocessing
3. Feature Engineering (hour, day extraction)
4. One-Hot Encoding (categorical variables)
5. Train-Test Split (80:20)
6. Model Training using Random Forest
7. Model Evaluation (MAE, MSE)
8. Prediction

---

## 📈 Evaluation Metrics

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit (for UI)

---

## 📁 Project Structure

```
Traffic_Flow_Prediction/
│
├── data/
│   └── traffic_data.xlsx
│
├── model/
│   ├── model.pkl
│   └── columns.pkl
│
├── train_model.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ How to Run the Project

### 🔹 Step 1: Install dependencies

```
pip install -r requirements.txt
```

### 🔹 Step 2: Train the model

```
python train_model.py
```

### 🔹 Step 3: Run the application

```
streamlit run app.py
```

---

## 🌐 Live Demo

👉 (Add your Streamlit deployment link here)

---

## 📷 Output

* Traffic prediction displayed based on input values
* User-friendly interface using Streamlit

---

## 🚀 Future Improvements

* Add real-time traffic data integration
* Improve accuracy using advanced models (XGBoost, Deep Learning)
* Deploy on cloud platforms for scalability

---

## 📌 Conclusion

The project demonstrates how machine learning can be used to predict traffic flow efficiently. Random Forest provides reliable results by handling complex relationships between features.

---

## 👨‍💻 Author

**Gowtham Vijay Sai Mamillapalli**

---
