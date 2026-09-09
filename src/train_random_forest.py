import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#1. Load dataset
df = pd.read_csv('data/dataset_phishing.csv')

df.columns = df.columns.str.strip()

#2 Target
if df['status'].dtype == 'object':
    y = df['status'].map({'phishing': 1, 'legitimate': 0})
else:
    y = df['status']

#3 Fitur
X_raw = df.drop(columns=['status'])
x = X_raw.select_dtypes(include=['number'])

print("Jumlah Data:", len(df))
print("Jumlah Fitur (X):", x.shape[1])
print("Distribusi Target:")
print(y.value_counts())

#4 Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y
)

#5 Train Model Random Forest
model = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
print("\nTraining Model Random Forest...")
model.fit(X_train, y_train)

#6 Prediction
y_pred = model.predict(X_test)

#7 Evaluation
print("==================================")
print("Evaluasi Model Random Forest...")
print("==================================")

print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['legitimate', 'phishing']))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\n==================================")
print("Daftar Fitur Model")
print("==================================")

for i, feature in enumerate(x.columns, start=1):
    print(f"{i}. {feature}")