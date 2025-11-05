import pandas as pd
import os

# Pfad zur CSV-Datei
csv_file = 'dataset_raw/Bank_Transaction_Fraud_Detection.csv'
pkl_file = 'Bank_Transaction_Fraud_Detection.pkl'

# CSV einlesen
print(f"Lese CSV-Datei: {csv_file}")
df = pd.read_csv(csv_file)

# Informationen über den DataFrame anzeigen
print(f"\nDataFrame Shape: {df.shape}")
print(f"Spalten: {df.columns.tolist()}")
print(f"\nErste Zeilen:")
print(df.head())

# Als PKL speichern
print(f"\nSpeichere als PKL-Datei: {pkl_file}")
df.to_pickle(pkl_file)

print(f"Erfolgreich gespeichert! Dateigröße: {os.path.getsize(pkl_file) / (1024*1024):.2f} MB")

# Optional: PKL-Datei wieder laden (zum Testen)
# df_loaded = pd.read_pickle(pkl_file)
# print(df_loaded.head())