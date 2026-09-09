import pandas as pd

df = pd.read_csv("data/dataset_phishing.csv")

print("Nama semua kolom:")
print(df.columns.tolist())

print("\nJumlah data per label:")
print(df["status"].value_counts())

print("\nContoh URL dan label:")
print(df[["url", "status"]].head(10))