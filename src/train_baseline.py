import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Load dataset
df = pd.read_csv('data/dataset_phishing.csv')

# Bersihkan nama kolom dari spasi yang tidak disengaja
df.columns = df.columns.str.strip()

# 2. Ambil target (y) terlebih dahulu
# Jika status berupa teks, konversi ke angka (phishing=1, legitimate=0)
if df['status'].dtype == 'object':
    y = df['status'].map({'phishing': 1, 'legitimate': 0})
else:
    y = df['status']

# 3. Pisahkan Fitur (X): Buang 'status' dari df asli, baru ambil kolom numerik
X_raw = df.drop(columns=['status'])
X = X_raw.select_dtypes(include=['number'])

# 4. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 5. Train Model Baseline (contoh: Random Forest)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 6. Evaluasi
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))