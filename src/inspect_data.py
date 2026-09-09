import pandas as pd

df = pd.read_csv('data/dataset_phishing.csv')

print("Ukuran Dataset:")
print(df.shape)

print("\n5 Data Pertama:")
print(df.head())

print("\nDaftar kolom:")
print(df.columns.tolist())

print("\nInformasi Dataset:")
print(df.info())