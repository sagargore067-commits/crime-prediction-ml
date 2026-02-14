import joblib
import pandas as pd

def predict_crime(state, district, year):
    model = joblib.load("models/trained_model.pkl")
    le_state, le_district = joblib.load("models/label_encoders.pkl")

    input_data = pd.DataFrame({
        "States/UTs": [le_state.transform([state])[0]],
        "District": [le_district.transform([district])[0]],
        "Year": [year]
    })

    prediction = model.predict(input_data)
    return round(prediction[0])
