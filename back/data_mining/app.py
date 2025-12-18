from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)

# Autoriser les requêtes Angular
CORS(app, origins=["http://localhost:4200"])

# Charger le modèle et les colonnes
model = joblib.load("model.pkl")
model_columns = joblib.load("model_columns.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    input_df = pd.DataFrame(columns=model_columns)
    input_df.loc[0] = 0

    for key, value in data.items():
        if key in input_df.columns:
            input_df.at[0, key] = value

    prediction = model.predict(input_df)

    return jsonify({
        "estimated_price": float(prediction[0])
    })

if __name__ == "__main__":
    app.run(debug=True)
