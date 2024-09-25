#1. Memuat Data
#a. Import/memasukkan script untuk library yang diperlukan yaitu 'Pandas'
import pandas as pd

#b. Buat Script untuk memuat data dari file CSV kedalam Data Frame
df = pd.read_csv('C:/Users/Acer/Downloads/movie_sample_dataset.csv')

#2. Memeriksa Data
#a. Tuliskan script untuk menampilkan beberapa baris pertama dari dataset untuk memahami struktur data
print(df.head())

#b. Lakukan Periksaan informasi umum tentang dataset, termasuk tipe data dan nilai yang hilang/missing value 
import numpy as np
# Kemudian tuliskan script untuk mengganti "nan" dengan " "
df['director_name'] = df['director_name'].replace(['Nan', 'Null'], '', regex=True)

# Lakukan pemeriksaan terhadap jumlah missing values di setiap kolom
print(df.isnull().sum())

#3. Membersihkan Data

#a. Menuliskan script untuk menghapus baris dengan missing values pada kolom "gross"
df_cleaned1 = df.dropna(subset=["gross"], axis=0, inplace=True)
# Melakukan reset index setelah menghapus baris
df.reset_index(drop=True, inplace=True)

#b. Menuliskan script untuk menghapus baris dengan missing values pada kolom "budget"
df_cleaned2 = df.dropna(subset=["budget"], axis=0, inplace=True)
# Melakukan reset index setelah menghapus baris
df.reset_index(drop=True, inplace=True)

#c. Mengatasi nilai yang tidak konsisten atau adanya kesalahan penulisan di kolom
# Contohnya yakni mengatasi perbedaan antara "Color" dan "color" serta "USA" dan "usa"
# Mengatasi perbedaan antara "Color" dan "color" atau inkonsistensi serupa pada kolom
# Misalnya, kita akan mengubah nilai dalam kolom "color" menjadi huruf kecil semua
if 'color' in df.columns:
    df['color'] = df['color'].str.lower()  # Ubah semua nilai di kolom "color" menjadi huruf kecil
print(df.head())

# Selanjutnya, mengubah nilai dalam kolom "usa" menjadi huruf "USA"/ huruf kapital semua
if 'country' in df.columns:
    df['country'] = df['country'].str.upper()  # script ini digunakan untuk mengubah semua nilai di kolom "usa" menjadi "USA"
print(df.head())

#d. Mengubah atau menghapus nilai-nilai yang tidak standar
# seperti adanya nilai negatif atau "NaN"

# Melakukan perubahan untuk nilai negatif pada kolom 'duration' dan 'imdb_score'
# Melakukan pergantian nilai negatif dengan NaN
df['duration'] = df['duration'].apply(lambda x: x if x >= 0 else np.nan)
df['imdb_score'] = df['imdb_score'].apply(lambda x: x if x >= 0 else np.nan)

# Mengganti dengan frekuensi pada kolom 'color', 'director name', dan 'genres', duration', dan 'imdb_score'
for column in ['color', 'director_name', 'genres', 'duration', 'imdb_score']:
    # Menentukan nilai yang paling sering muncul (mode/modus)
    mode_value = df[column].mode()[0]
    # Mengganti nilai N/A dengan nilai yang paling sering muncul (modus)
    df[column].fillna(mode_value, inplace=True)
    mode_value = df['director_name'].mode()[0]  # Script untuk mendapatkan nilai yang paling sering muncul
    df['director_name'].replace('', mode_value, inplace=True)  # script untuk mengganti string kosong dengan mode

#4. Melakukan Transformasi Data
#a. Lakukan perubahan tipe data kolom menjadi tipe data yang sesuai (misalnya, konversi genres dari object ke string).
# agar bisa dilakukan pemisahan genre yang tergabung dalam satu kolom menjadi beberapa kolom
print(df.dtypes)
df['genres'] = df['genres'].astype(str)
print(df['genres'])


#Tidak ada yang diubah karena tipe data sudah sesuai
#Variabel numerik (int atau float) dan variabel kategorik (string atau object)

#b. Melakuakan Normalisasi Teks untuk Memastikan Konsistensi
# (Contohnya mengubah teks menjadi huruf kecil)
# Melakukan normalisasi teks untuk kolom 'color', 'director_name', 'genres', 'movie_title',
# 'language', 'country', dan 'actors'
columns_to_normalize = ['color', 'director_name', 'genres', 'movie_title', 'language', 'country', 'actors']

for column in columns_to_normalize:
    df[column] = df[column].str.lower()  # Script untuk mengubah teks menjadi huruf kecil
    df[column] = df[column].str.strip()  # Script untuk menghapus spasi di awal dan akhir teks

#5. Melakukan Penyimpanan Data
df.to_csv('C:/Users/Acer/Downloads/movie_dataset_cleaned.csv', index=False)