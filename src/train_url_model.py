import pandas as pd
import joblib
from feature_extraction import extract_basic_features
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# 1. Load dataset
df = pd.read_csv("data/dataset_phishing.csv")

df.columns = df.columns.str.strip()

# 2. Target
y = df["status"]

# Ambil daftar fitur yang benar-benar bisa dihasilkan extractor
test_features = extract_basic_features("https://example.com")

url_features = [
    feature
    for feature in test_features.keys()
    if feature != "ip" and feature in df.columns
]

X = df[url_features]

print("Fitur yang dipakai model:")
for i, feature in enumerate(url_features, start=1):
    print(f"{i}. {feature}")

print("\nJumlah Fitur:", len(url_features))

X = df[url_features]

print("Jumlah Data:", len(df))
print("Jumlah Fitur:", X.shape[1])

print("\nDistribusi Target:")
print(y.value_counts())

# 4. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 5. Random Forest
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

print("\nTraining URL-only Random Forest...")

model.fit(X_train, y_train)

print("Training selesai!")

# 6. Prediksi
y_pred = model.predict(X_test)

# 7. Evaluasi
print("\n==================================")
print("URL-ONLY RANDOM FOREST")
print("==================================")

print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=["legitimate", "phishing"]
    )
)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Simpan model
joblib.dump(model, "models/phishing_model.pkl")

# Simpan daftar fitur
joblib.dump(url_features, "models/url_features.pkl")

print("\nModel berhasil disimpan!")
print("models/phishing_model.pkl")
print("models/url_features.pkl")