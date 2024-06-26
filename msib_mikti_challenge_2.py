# -*- coding: utf-8 -*-
"""MSIB MIKTI Challenge 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qLBuDP6h9T-dJSrjwzp5UW7RqAxiJnkV

Lanngkah Pertama : Import Library Numpy dan Pandas
"""

import pandas as pd
import numpy as np

# Membaca file CSV dan menampilkan 5 data teratas
df = pd.read_csv("Property Listing Dataset.csv")
df.head()

"""Langkah Kedua : Cek values tiap kolom, dan kolom yabg kosong di isi dengan N/A"""

# Mencari value null/kosong tiap kolom dan menjumlahkannya pada tiap kolom
jml_null = df.isnull().sum()
jml_null

# Mengganti value kosong dengan nilai 'N/A'
df = df.fillna('N/A')
df.head()

# Sudah Tidak ada value kosong dala setiap kolom
df.isnull().sum()

"""Langkah Ketiga : Melakukan Check terhadap Duplikat data dan menghapus salah satunya"""

# Menghitung jumlah data duplikat
duplikat = df.duplicated().sum()
print(f'Jumlah data duplikat(sebelum dihapus) : {duplikat}')

# Menghapus data duplikat
df = df.drop_duplicates()
print(f'Jumlah data duplikat(sebelum dihapus) : {df.duplicated().sum()}')

"""Langkah Ketiga : Pastikan value pada kolom 'Rooms', 'Bathrooms', 'Car Parks' Harus menggunakan tipe data number, jika ada value yang tidak menggunakan tipe data number maka di hapus"""

df.info()

# Menampilkan nilai unik pada kolom 'Rooms'
df['Rooms'].unique()

# Membersihkan nilai-nilai non-angka
df['Rooms'] = df['Rooms'].str.replace('2\+1|N/A|Studio|5\+1|3\+1', '')

# Mengonversi ke tipe data integer
df['Rooms'] = pd.to_numeric(df['Rooms'], errors='coerce')

# Mengatasi nilai-nilai yang tidak dapat dikonversi menjadi integer
df['Rooms'] = df['Rooms'].fillna(0).astype(int)

df['Rooms'].unique()

# Menampilkan nilai unik pada kolom 'Bathrooms'
df['Bathrooms'].unique()

# Mengganti 'N/A' dengan NaN
df['Bathrooms'] = df['Bathrooms'].replace('N/A', np.nan)

# Mengonversi ke tipe data integer
df['Bathrooms'] = df['Bathrooms'].astype(float)

df['Bathrooms'].unique()

# Menampilkan nilai unik pada kolom 'Car parks'
df['Car Parks'].unique()

# Mengganti string kosong dengan NaN
df['Car Parks'] = df['Car Parks'].replace('', np.nan)

# Mengonversi ke tipe data float
df['Car Parks'] = df['Car Parks'].astype(float)

df['Car Parks'].unique()

df.head(10)

