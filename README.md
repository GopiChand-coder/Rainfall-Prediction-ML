🌧 Rainfall Prediction Web Application

🎥 Demo Video: https://drive.google.com/file/d/1bpNTpYRhcwpFVrPLMM-1t9K93HwU_FI4/view?usp=sharing

📌 Project Overview

This project is a Machine Learning based Rainfall Prediction System built using the Weather Australia Dataset.

The application predicts whether it will rain tomorrow based on various meteorological parameters such as temperature, humidity, pressure, wind speed, and rainfall.

The model is deployed as a Flask Web Application, allowing users to input weather data and get real-time predictions.






🚀 Features

Data preprocessing and cleaning

Missing value handling

Feature engineering (year, month, day extraction)

Label encoding for categorical features

Feature scaling using StandardScaler

Machine Learning model training

Model saving using Pickle

Flask-based web deployment

Dynamic result rendering (Rain / No Rain)

🛠 Technologies Used

Python

Pandas

NumPy

Scikit-learn

Matplotlib & Seaborn

Flask

HTML

Pickle / Joblib

🧠 Machine Learning Workflow

1️⃣ Data Preprocessing

Handled missing values using mean imputation

Converted categorical features using Label Encoding

Extracted year, month, and day from Date column

Scaled numerical features using StandardScaler

2️⃣ Model Training

Split dataset into training and testing sets

Trained classification model

Evaluated using:

Accuracy

Precision

Recall

F1 Score

3️⃣ Model Saving

pickle.dump(model, open('Rainfall.pkl', 'wb'))

pickle.dump(scale, open('scale.pkl', 'wb'))

🌐 Flask Deployment Process

Initialize Flask app

Load saved model and scaler

Create routes:

/ → Home page

/predict → Prediction logic

Collect user input from HTML form

Convert input into DataFrame

Scale input data

Predict result

Render result page

▶️ How to Run the Project

Step 1: Clone Repository

git clone https://github.com/GopiChand-coder/Rainfall-Prediction-ML.git

cd rainfall-prediction

Step 2: Create Virtual Environment

python -m venv venv

source venv/bin/activate   # Mac/Linux

venv\Scripts\activate      # Windows

Step 3: Install Dependencies

pip install -r requirements.txt

Step 4: Run Flask App

python app.py

Open browser:

http://127.0.0.1:5000/

🔮 Sample Prediction

Input:

High humidity

Low pressure

Rain today

Strong winds

Output:

Chances of rain tomorrow.

📌 Dataset

Dataset used: Weather Australia Dataset (weatherAUS.csv)

Target Variable:

RainTomorrow

Classes:

0 → No Rain

1 → Rain

🎯 Future Improvements

Add cloud deployment (IBM Cloud / AWS)

Improve UI design

Add real-time weather API integration

Add probability visualization graph

Use advanced ML models (XGBoost, Random Forest)

👨‍💻 Author

Gopi Chand

Machine Learning & AI Enthusiast

⭐ If you like this project

Give it a ⭐ on GitHub!
