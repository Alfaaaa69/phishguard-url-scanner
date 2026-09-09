import pandas as pd
from feature_extraction import extract_basic_features


# Load dataset
df = pd.read_csv("data/dataset_phishing.csv")
df.columns = df.columns.str.strip()

# Ambil beberapa baris untuk diuji
sample = df.head(10)

print("=" * 60)
print("VALIDASI FEATURE EXTRACTOR")
print("=" * 60)

for index, row in sample.iterrows():
    url = row["url"]

    extracted = extract_basic_features(url)

    print(f"\nURL #{index + 1}")
    print(url)

    mismatch = 0

    for feature, extracted_value in extracted.items():
        dataset_value = row[feature]

        # Untuk float, beri toleransi kecil
        if isinstance(extracted_value, float):
            same = abs(extracted_value - dataset_value) < 0.0001
        else:
            same = extracted_value == dataset_value

        if not same:
            mismatch += 1
            print(
                f"[BEDA] {feature}: "
                f"extractor={extracted_value} | "
                f"dataset={dataset_value}"
            )

    if mismatch == 0:
        print("[OK] Semua fitur cocok")
    else:
        print(f"[!] Total fitur berbeda: {mismatch}")