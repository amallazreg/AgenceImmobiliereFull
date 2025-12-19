# 🏠 Agence Immobilière – Application Full Stack avec Estimation de Prix

## 📌 Description du projet

Ce projet est une application **Full Stack de gestion immobilière** intégrant un **module d’estimation automatique de prix basé sur l’Intelligence Artificielle**.

L’objectif est de permettre aux utilisateurs de :
- Consulter et gérer des annonces immobilières  
- Estimer automatiquement le prix d’un bien immobilier (vente ou location)  
- Obtenir une estimation basée sur plusieurs critères :
  - Surface  
  - Type de bien  
  - Type de transaction (vente / location)  
  - Localisation  

---

## 🧱 Architecture du projet

```bash
AgenceImmobiliereFull/
│
├── front/                  # Frontend Angular
│   ├── src/
│   ├── services/
│   └── components/
│
├── back/
│   ├── api/                # Backend principal (gestion des annonces)
│   └── data_mining/        # IA & prédiction de prix
│       ├── data_extraction.py
│       ├── model.pkl
│       ├── model_columns.pkl
│       └── app.py
│
```
## ⚙️ Technologies utilisées

### Frontend
- Angular
- TypeScript
- HTML / CSS
- HttpClient

### Backend
- Python 3.11
- Flask (API REST)
- MongoDB (base de données)
- PyMongo

### Data Mining / IA
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

## ✅ Prérequis

Avant de commencer, assurez-vous d’avoir installé :
- Node.js (>= 16)
- Angular CLI
- Python 3.10+
- MongoDB (local)
- Git

---

## 📥 Installation du projet

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/amallazreg/AgenceImmobiliereFull.git
cd AgenceImmobiliereFull
```
## 🔙 Backend – Installation & Lancement

### Accéder au dossier backend

```bash
cd back/data_mining
```
### Installer les dépendances Python

```bash
pip install flask pandas numpy scikit-learn pymongo joblib flask-cors
```

### Entraîner le modèle IA 
```bash
python data_extraction.py
```
➡Cela génère : - model.pkl - model_columns.pkl

### ▶️ Lancer l’API de prédiction

Une fois le modèle entraîné, lancez l’API Flask afin de permettre la prédiction des prix immobiliers.

```bash
python app.py
```
API disponible sur :
```bash
http://127.0.0.1:5000/predict
```
## 🎨 Frontend – Installation & Lancement

### Accéder au frontend

```bash
cd front
```
### Installer les dépendances Angular 
```bash
npm install
```
### Lancer l’application Angular
```bash
ng serve
```
Application disponible sur : 
```bash
http://localhost:4200
```
## 🔄 Fonctionnement global

1. L’utilisateur saisit les caractéristiques du bien (surface, type, transaction, localisation)  
2. Angular envoie les données au backend Flask  
3. Flask prépare les features selon le modèle entraîné  
4. Le modèle IA prédit le prix estimé  
5. Le résultat est renvoyé et affiché en temps réel sur l’interface
