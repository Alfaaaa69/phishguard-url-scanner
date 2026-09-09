# PhishGuard AI

PhishGuard AI adalah aplikasi web berbasis Flask yang mendeteksi URL phishing menggunakan Machine Learning (Random Forest Classifier). Aplikasi ini menganalisis struktur URL dan menampilkan skor risiko phishing secara real-time.

## Features

- **URL Analysis** - Ekstraksi 30+ fitur struktural dari URL
- **Machine Learning** - Klasifikasi phishing menggunakan Random Forest
- **Risk Scoring** - Skor phishing 0-100% dengan level risiko (LOW/MEDIUM/HIGH)
- **Reason Explanation** - Penjelasan alasan mengapa URL dianggap mencurigakan
- **Modern UI** - Interface responsif dengan animasi progress bar

## Tech Stack

- **Backend**: Python, Flask
- **ML Model**: Random Forest (scikit-learn, joblib)
- **Frontend**: HTML, CSS, JavaScript
- **Data**: dataset_phishing.csv

## Project Structure

```
PhishGuard/
├── app.py                    # Flask application
├── src/
│   ├── feature_extraction.py # URL feature extraction
│   ├── train_random_forest.py
│   └── ...
├── models/
│   ├── phishing_model.pkl    # Trained ML model
│   └── url_features.pkl      # Feature list
├── data/
│   └── dataset_phishing.csv  # Training dataset
├── templates/
│   └── index.html            # Main UI
└── static/
    └── css/
        └── style.css         # Styling
```

## Installation

### 1. Clone repository

```bash
git clone https://github.com/Alfaaaa69/phishguard-url-scanner.git
cd phishguard-url-scanner
```

### 2. Install dependencies

```bash
pip install flask pandas joblib scikit-learn
```

### 3. Run the application

```bash
python app.py
```

### 4. Open browser

Buka `http://localhost:5000`

## Usage

1. Buka aplikasi di browser
2. Masukkan URL yang ingin dianalisis
3. Klik "Analyze URL"
4. Lihat hasil analisis meliputi:
   - Prediksi (Phishing / Legitimate)
   - Skor phishing (0-100%)
   - Level risiko (LOW / MEDIUM / HIGH)
   - Alasan analisis

## Features Extracted

| Feature | Deskripsi |
|---------|-----------|
| `length_url` | Panjang URL |
| `length_hostname` | Panjang hostname |
| `ip` | Apakah hostname IP address |
| `nb_dots`, `nb_hyphens`, `nb_at` | Jumlah karakter tertentu |
| `ratio_digits_url` | Rasio digit dalam URL |
| `nb_subdomains` | Jumlah subdomain |
| `punycode` | Penggunaan punycode |
| `https_token` | Apakah menggunakan HTTPS |
| `prefix_suffix` | Tanda hubung di hostname |

## Model

Model Random Forest dilatih menggunakan dataset phishing dan disimpan dalam format `.pkl` menggunakan joblib.

## License

MIT License
