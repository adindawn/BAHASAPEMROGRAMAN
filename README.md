# BIODATA
NAMA  = Adinda Aulia Nabila Putri
KELAS = TI.24.A.4
NIM   = 312410309

# Program Bilangan Terbesar
program ini adalah sebuah aplikasi sederhana untuk menentukan bilangan terbesar dari sejumlah input yang diberikan oleh pengguna. program akan terus meminta pengguna untuk memasukkan bilangan sampai pengguna memasukkan angka 0, jika pengguna memasukka angka 0, program akan berhenti dan menampilkan bilangan terbesar yang telah dimasukkan.

# Contoh Penggunaan
bilangan_terbesar = float('-inf')

while True:
    bilangan = float(input("masukkan bilangan  (tekan 0 untuk berhenti): "))
    if bilangan == 0:
        break
    if bilangan > bilangan_terbesar:
       bilangan_terbesar = bilangan 

if bilangan_terbesar == float('-inf'):
    print("Tidak ada bilangan yang dimasukkan.")
else:
   print("Bilangan terbesar adalah:", bilangan_terbesar)


Masukkan bilangan (tekan 0 untuk berhenti): 80
Masukkan bilangan (tekan 0 untuk berhenti): 60
Masukkan bilangan (tekan 0 untuk berhenti): 20
Masukkan bilangan (tekan 0 untuk berhenti): 0
Bilangan terbesar adalah : 80.0

# Berikut Hasil Screenshotnya 














# Berikut Hasil Flowchartnya















# Persyaratannya 
  * Pyton 3.x harus sudah teristal di sistem

# Cara Menjalakannya 
  1. Pastikan Pyton sudah ter-instal di komputer
  2. Simpan kode program dalam file bernama pemprograman.py
  3. Bukan terminal atau command prompt
  4. Jalankan program dengan perintah berikut:
         python pemrograman.py

# Menentukan 3 Bilangan Terbesar
program ini di gunakan untuk menentukan bilangan tebesar dari tiga bilangan yang dimasukkan oleh pengguna. Program meminta tiga bilangan sebagai input, membandingkannya, dan kemudian mencetak bilangan terbesar diantara ketiga bilangan tersebut.

# Kode Program
a = int(input('Masukkan bilangan pertama: '))
b = int(input('Masukkan bilangan kedua: '))
c = int(input('Masukkan bilangan ketiga: '))

if a > b and a > c:
    print(f'Bilangan terbesar adalah {a}')
elif b > a and b > c:
    print(f'Bilangan terbesar adalah {b}')
else:
    print(f'Bilangan terbesar adalah {c}')

# Hasil Screenshot di Visual Studio Code 


