import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

def train():

    df = pd.read_csv("data/crime_data.csv")

    df = df[["States/UTs", "District", "Year", "Total Cognizable IPC crimes"]]
    df = df.dropna()

    le_state = LabelEncoder()
    le_district = LabelEncoder()

    df["States/UTs"] = le_state.fit_transform(df["States/UTs"])
    df["District"] = le_district.fit_transform(df["District"])

    X = df[["States/UTs", "District", "Year"]]
    y = df["Total Cognizable IPC crimes"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    r2 = r2_score(y_test, model.predict(X_test))
    print("Model R2 Score:", round(r2, 3))

    joblib.dump(model, "models/trained_model.pkl")
    joblib.dump((le_state, le_district), "models/label_encoders.pkl")

if __name__ == "__main__":
    train()
