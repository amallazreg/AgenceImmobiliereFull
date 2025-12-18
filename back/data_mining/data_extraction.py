from pymongo import MongoClient
import pandas as pd
import re
import joblib




from pymongo import MongoClient
import pandas as pd
import re

# Connexion MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["agence"]          
collection = db["annonces"]         

data = []

for doc in collection.find():
    surface = int(re.sub(r"\D", "", doc["surface"]))
    prix = int(doc["prix"])
    type_bien = doc["type"]
    transaction = doc["transactionType"]
    localisation = doc["adresse"]  

    data.append({
        "surface": surface,
        "type": type_bien,
        "transaction": transaction,
        "localisation": localisation,
        "prix": prix
    })

df = pd.DataFrame(data)

print("Dataset brut :")
print(df.head())



from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Encodage des variables catégorielles
df_encoded = pd.get_dummies(
    df,
    columns=["type", "transaction", "localisation"],
    drop_first=True
)

print("\nDataset encodé :")
print(df_encoded.head())

# Séparation X / y
X = df_encoded.drop("prix", axis=1)
y = df_encoded["prix"]

# Split train / test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Entraînement du modèle
model = LinearRegression()
model.fit(X_train, y_train)

# Prédictions
y_pred = model.predict(X_test)

print("\nPrix réels :", list(y_test))
print("Prix prédits :", list(y_pred))

# Évaluation
mae = mean_absolute_error(y_test, y_pred)
print("\nErreur moyenne absolue (MAE) :", mae)

joblib.dump(model, "model.pkl")
print("\nModèle sauvegardé dans model.pkl")

# Sauvegarder les colonnes du modèle
joblib.dump(list(X.columns), "model_columns.pkl")
print("Colonnes sauvegardées dans model_columns.pkl")
