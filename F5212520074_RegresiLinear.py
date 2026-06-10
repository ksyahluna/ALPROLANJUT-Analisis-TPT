# TUGAS ALPRO LANJUT 
# Nama : Kissya Syahluna Rahim 
# Nim : F5212520074
# Kelas : Si B

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

print("="*50)
print("TUGAS REGRESI LINEAR")
print("Nama  : Kissya Syahluna Rahim")
print("NIM   : F5212520074")
print("Kelas : SI B")
print("="*50)

# Membaca dataset
df = pd.read_excel(
    "dataset nya ini yaaa.xlsx",
    sheet_name="Sheet1"
)

# Menampilkan data Kota Palu
print(df[df["Kabupaten/Kota"] == "Kota Palu"])

# Variabel X dan Y
X = df[["TPT (%)"]]
Y = df["Persentase Penduduk Miskin (%)"]

# Membuat model regresi
model = LinearRegression()
model.fit(X, Y)

# Menampilkan hasil model
print("\nHASIL REGRESI")
print("Intercept =", model.intercept_)
print("Koefisien TPT =", model.coef_[0])

# Prediksi
prediksi = model.predict(X)

# Nilai R²
r2 = r2_score(Y, prediksi)
print("R² =", r2)

# Menambahkan hasil prediksi ke dataframe
df["Prediksi Kemiskinan (%)"] = prediksi

print("\nHASIL PREDIKSI")
print(df)

# Prediksi per kabupaten/kota berdasarkan data tahun terakhir
print("\nPREDIKSI SETIAP KABUPATEN/KOTA")

for daerah in df["Kabupaten/Kota"].unique():

    data_daerah = df[df["Kabupaten/Kota"] == daerah]

    terakhir = data_daerah.sort_values(
        "Tahun"
    ).iloc[-1]

    X_pred = pd.DataFrame({
        "TPT (%)": [terakhir["TPT (%)"]]
    })

    hasil = model.predict(X_pred)[0]

    print(
        f"{daerah:<25} : "
        f"{hasil:.2f}%"
    )