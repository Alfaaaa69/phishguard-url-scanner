from flask import Flask, render_template, request 
import joblib
import pandas as pd

from src.feature_extraction import extract_basic_features

app = Flask(__name__)

# Load model dan daftar fitur
model = joblib.load("models/phishing_model.pkl")
url_features = joblib.load("models/url_features.pkl")


def get_reasons(extracted):
    reasons = []

    if extracted.get("length_url", 0) > 75:
        reasons.append("URL is unusually long")

    if extracted.get("nb_at", 0) > 0:
        reasons.append("URL contains @ symbol")

    if extracted.get("nb_hyphens", 0) >= 3:
        reasons.append("URL contains many hyphens")

    if extracted.get("nb_subdomains", 0) >= 3:
        reasons.append("URL contains multiple subdomains")

    if extracted.get("ratio_digits_url", 0) > 0.3:
        reasons.append("URL contains a high number of digits")

    if extracted.get("https_token", 0) == 1:
        reasons.append("URL does not use HTTPS")

    if extracted.get("punycode", 0) == 1:
        reasons.append("Domain uses punycode encoding")

    if extracted.get("port", 0) == 1:
        reasons.append("URL uses an explicit port")

    if extracted.get("prefix_suffix", 0) == 1:
        reasons.append("Domain contains a hyphen")

    if not reasons:
        reasons.append("No obvious suspicious URL patterns were found")

    return reasons


def analyze_url(url):
    extracted = extract_basic_features(url)

    reasons = get_reasons(extracted)
    input_data = {
        feature: extracted[feature]
        for feature in url_features
    }

    X_input = pd.DataFrame([input_data])

    prediction = model.predict(X_input)[0]
    probabilities = model.predict_proba(X_input)[0]

    probability_map = {
        label: prob
        for label, prob in zip(model.classes_, probabilities)
    }

    phishing_score = probability_map.get("phishing", 0) * 100

    if phishing_score >= 75:
        risk_level = "HIGH"
    elif phishing_score >= 40:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "prediction": prediction,
        "phishing_score": phishing_score,
        "risk_level": risk_level,
        "reasons": reasons
    }


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    url = ""

    if request.method == "POST":
        url = request.form.get("url", "").strip()

        if url:
            result = analyze_url(url)

    return render_template(
        "index.html",
        result=result,
        url=url
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)