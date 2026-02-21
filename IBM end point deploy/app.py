import numpy as np
import pandas as pd
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

model = pickle.load(open('rainfall.pkl', 'rb'))
scaler = pickle.load(open('scale.pkl', 'rb'))
encoder = pickle.load(open('encoder.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    try:
        input_features = [
            float(request.form['Location']),
            float(request.form['MinTemp']),
            float(request.form['MaxTemp']),
            float(request.form['Rainfall']),
            float(request.form['WindGustSpeed']),
            float(request.form['WindSpeed9am']),
            float(request.form['WindSpeed3pm']),
            float(request.form['Humidity9am']),
            float(request.form['Humidity3pm']),
            float(request.form['Pressure9am']),
            float(request.form['Pressure3pm']),
            float(request.form['Temp9am']),
            float(request.form['Temp3pm']),
            float(request.form['RainToday']),
            float(request.form['WindGustDir']),
            float(request.form['WindDir9am']),
            float(request.form['WindDir3pm']),
            float(request.form['year']),
            float(request.form['month']),
            float(request.form['day'])
        ]

        column_names = [
            'Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'WindGustSpeed',
            'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
            'Pressure9am', 'Pressure3pm', 'Temp9am', 'Temp3pm',
            'RainToday', 'WindGustDir', 'WindDir9am', 'WindDir3pm',
            'year', 'month', 'day'
        ]

        data = pd.DataFrame([input_features], columns=column_names)

        training_columns = [
            'MinTemp', 'MaxTemp', 'Rainfall', 'WindGustSpeed',
            'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
            'Pressure9am', 'Pressure3pm', 'Temp9am', 'Temp3pm'
        ]
        
        data_for_scaling = data[[col for col in training_columns if col in data.columns]]

        data_scaled = scaler.transform(data_for_scaling)

        prediction = model.predict(data_scaled)[0]
        probabilities = model.predict_proba(data_scaled)[0]
        
        confidence = max(probabilities) * 100
        
        predicted_class = encoder.inverse_transform([prediction])[0]
        
        class_probs = {}
        for idx, class_name in enumerate(encoder.classes_):
            class_probs[class_name] = probabilities[idx] * 100
        
        if predicted_class == 'Yes':
            return render_template('chance.html', 
                                 prediction=predicted_class,
                                 confidence=confidence,
                                 class_probs=class_probs)
        else:
            return render_template('noChance.html',
                                 prediction=predicted_class,
                                 confidence=confidence,
                                 class_probs=class_probs)
    
    except KeyError as e:
        return f"Error: Missing form field {str(e)}", 400
    except Exception as e:
        return f"Error: {str(e)}", 400

if __name__ == "__main__":
    app.run(debug=True)
