import joblib
import pandas as pd

from feature_extraction import extract_basic_features

#load model
model = joblib.load("models/phishing_model.pkl") 
url_features = joblib.load("models/url_features.pkl")
def predict_url(url):
    # Extract fitur dari URL
    extracted = extract_basic_features(url)

    # Ambil hanya fitur yang dipakai model
    input_data = {
        feature: extracted[feature]
        for feature in url_features
    }

    # Jadikan DataFrame agar nama + urutan fitur sesuai training
    X_input = pd.DataFrame([input_data])

    # Prediksi kelas
    prediction = model.predict(X_input)[0]

    # Probabilitas
    probabilities = model.predict_proba(X_input)[0]

    classes = model.classes_

    probability_map = {
        label: prob
        for label, prob in zip(classes, probabilities)
    }

    return prediction, probability_map


if __name__ == "__main__":
    url = input("Masukkan URL: ").strip()

    prediction, probabilities = predict_url(url)

    # Ambil nilai probabilitas untuk "phishing" (atau label 1 jika dalam bentuk angka)
    phishing_score = (probabilities.get("phishing", probabilities.get(1, 0))) * 100

    if phishing_score >= 75:
        risk_level = "HIGH"
    elif phishing_score >= 40:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    print("\n==================================")
    print("PHISHGUARD RESULT")
    print("==================================")

    print("URL:", url)
    print("Prediction:", prediction)
    print(f"Phishing Risk: {phishing_score:.2f}%")
    print("Risk Level:", risk_level)