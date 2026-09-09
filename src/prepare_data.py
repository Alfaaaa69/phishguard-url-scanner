import pandas as pd
from sklearn.model_selection import train_test_split

# 1. Load the dataset
df = pd.read_csv('data/dataset_phishing.csv')

# Rapikan nama kolom dari spasi yang tidak disengaja
df.columns = df.columns.str.strip()

# 2. Pisahkan Target (y) terlebih dahulu
y = df['status']

# 3. Pisahkan Fitur (X) dari DataFrame utama, lalu filter kolom numeriknya
X_raw = df.drop(columns=['status'])
X = X_raw.select_dtypes(include=['number'])

print("Jumlah Fitur (X):", X.shape[1])
print("Jumlah Target (y):", y.shape[0])

print("\nDistribusi Label:")
print(y.value_counts())

# 4. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("\nUkuran Dataset Training:", X_train.shape[0])
print("Ukuran Dataset Testing:", X_test.shape[0])