# BIODATA
NAMA  = Adinda Aulia Nabila Putri
KELAS = TI.24.A.4
NIM   = 312410309

# Program Bilangan Terbesar
program ini adalah sebuah aplikasi sederhana untuk menentukan bilangan terbesar dari sejumlah input yang diberikan oleh pengguna.
program akan terus meminta pengguna untuk memasukkan bilangan sampai pengguna memasukkan angka 0, jika pengguna memasukka angka 0, 
program akan berhenti dan menampilkan bilangan terbesar yang telah dimasukkan.

# Contoh Penggunaan

```PYTHON
(bilangan_terbesar = float('-inf')  

while True:
    bilangan = float(input("Masukkan bilangan (tekan 0 untuk berhenti): "))
    if bilangan == 0:
        break   
    if bilangan > bilangan_terbesar:
        bilangan_terbesar = bilangan

if bilangan_terbesar == float('-inf'):
    print("Tidak ada bilangan yang dimasukkan.")
else:
    print("Bilangan terbesar adalah:", bilangan_terbesar) )
````

    
  Masukkan bilangan (tekan 0 untuk berhenti): 80
  Masukkan bilangan (tekan 0 untuk berhenti): 60
  Masukkan bilangan (tekan 0 untuk berhenti): 20
  Masukkan bilangan (tekan 0 untuk berhenti): 0
  Bilangan terbesar adalah : 80.0


# Berikut Hasil di Visual Studio Code

    ![Screenshot 2024-10-19 095852](https://github.com/user-attachments/assets/18c4eb26-8df1-45df-afb3-dee64f83a5f9)









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
program ini di gunakan untuk menentukan bilangan tebesar dari tiga bilangan yang dimasukkan oleh pengguna.
Program meminta tiga bilangan sebagai input, membandingkannya, 
dan kemudian mencetak bilangan terbesar diantara ketiga bilangan tersebut.

# Kode Program
```PYTHON
(a = int(input('Masukkan bilangan pertama: '))
b = int(input('Masukkan bilangan kedua: '))
c = int(input('Masukkan bilangan ketiga: '))

if a > b and a > c:
    print(f'Bilangan terbesar adalah {a}')
elif b > a and b > c:
    print(f'Bilangan terbesar adalah {b}')
else:
    print(f'Bilangan terbesar adalah {c}') )
````

    
# Hasil Screenshot di Visual Studio Code 
   
      ![WhatsApp Image 2024-10-21 at 08 21 06 (1)](https://github.com/user-attachments/assets/0ac9c3a8-aa3c-407b-974d-f764c3ae921f)








# Berikut adalah Flowchartnya

















# Penjelasannya Kode
  1. Input Bilangan: Program meminta pengguna memasukkan tiga bilangan menggunakan fungsi input()
     dan mengonversinya menjadi bilangan bulat (int), 
     kemudian di simpan ke variable a, b, dan c.
  3. Logika Penentuan Bilangan Terbesar:
         * Program menggunakan struktur kondisi if-elif-else untuk membandingkan ketiga bilangan.
         * Bilangan A lebih besar dari B dan C, program akan mencetak bahwa A adalah bilangan terbesar.
         * jika B lebihb besar dari A dan C, program akan mencetak bahwa B adalah bilangan terbesar.
         * Jika tidak ada kondisi yang terpenuhi, program akan menganggap bahwa C adalah bilangan terbesar dan mencetaknya.
  4. Output: Program akan mencetak bilangan terbesar yang ditemukan
     di antara ketiga bilangan yang diinputkan oleh pengguna.

# Contoh Eksekusi Program
# Contoh 1:

     Pengguna memasukkan tiga bilangan, yaitu 30, 60, 10

     Masukkan bilangan pertama: 30
     Masukkan bilangan kedua: 60
     Masukkan bilangan ketiga: 10
     Bilangan terbesar adalah 60

# Contoh 2:

    Pengguna memasukkan tiga bilangan, yaitu 50, 70, 90

    Masukkan bilangan pertama: 50
    Masukkan bilangan kedua: 70
    Masukkan bilangan keetiga: 90
    Bilangan terbesar adalah 90



![WhatsApp Image 2024-10-21 at 08 28 05 (1)](https://github.com/user-attachments/assets/f5a9fdba-39d9-4799-9e1b-0e2aa9195f9e)







# Praktikum 3
# LATIHAN 1
    ![WhatsApp Image 2024-10-21 at 08 28 05](https://github.com/user-attachments/assets/cabd5ebf-04df-4f7e-81b3-46b223e3b0ca)






``` PYTHON
(#penggunaan end
print('A', end='')
print('B', end='')
print('C', end='')
print()
print('X')
print('Y')
print('z')

#penggunaan separator
w, x, y, z = 10, 15, 20, 25
print(w, x, y, z)
print(w, x, y, z, sep=',')
print(w, x, y, z, sep='')
print(w, x, y, z, sep=':')
print(w, x, y, z, sep='.....') )
````




Parameter end dalam fungsi Print() di Python di gunakan untuk menambahkan string("")apapun diakhiri dan mengeluarkan pertanyaan print

Print()

secara default, fungsi Print() akan mengakhiri dengan baris baru, dan akan secra otomatis karakter baris baru di akhir outputnya.

berikut hasil screenshot dari pemrograman Penggunaan END

   ![WhatsApp Image 2024-10-21 at 07 57 20 (1)](https://github.com/user-attachments/assets/55276792-b599-4429-a647-d6fe006428bd)


Penggunaan Seperator ini menentukan pembatasan yang digunakan untuk memisahkan sting, seperator dapat berupa karakter. Jika tidak ditemukan, maka python akan menggunakan spasi sebagai pemisah.

berikut hasil screenshot dari pemrograman penggunaan seperator 

   ![WhatsApp Image 2024-10-21 at 08 40 57](https://github.com/user-attachments/assets/20b1d674-69ce-436c-936e-d7f049bbb9f8)


w, x, y, z,= 10, 15, 20, 25 

Variable yang seperti ini menentukan parameter, jadi variable ini tidak bisa memasukkan angka yang sudah di tentukan w=10, x=15, y=20, z=25 

  print(w, x, y, z,)

Fungsi ini hanya mencetak saja yang menggunakan fungsi print(), tetapi di karenakan mencetak parameter, koma tersebut di hilangkan. 

   print(w, x, y, z, sep=',')

Karena pemisahannya dihilangkan, kita menggunakan fungsi sep atau split() dan kita memasukkan pemisahnya dalam string akan memunculkan cetakan yang sesuai keinginan anda dalam mamisahkan sesuatu parameter.

# String Format 

 ![WhatsApp Image 2024-10-21 at 08 51 52 (1)](https://github.com/user-attachments/assets/99af9023-8ef2-43ed-b069-896736e8e5d8)



```PYTHON
print(0, 10**0)
print(1, 10**1)
print(2, 10**2)
print(3, 10**3)
print(4, 10**4)
print(5, 10**5)
print(6, 10**6)
print(7, 10**7)
print(8, 10**8)
print(9, 10**9)
print(10, 10**10)

print('{0:>3} {1:>16}'.format(0, 10**0))
print('{0:>3} {1:>16}'.format(1, 10**1))
print('{0:>3} {1:>16}'.format(2, 10**2))
print('{0:>3} {1:>16}'.format(3, 10**3))
print('{0:>3} {1:>16}'.format(4, 10**4))
print('{0:>3} {1:>16}'.format(5, 10**5))
print('{0:>3} {1:>16}'.format(6, 10**6))
print('{0:>3} {1:>16}'.format(7, 10**7))
print('{0:>3} {1:>16}'.format(8, 10**8))
print('{0:>3} {1:>16}'.format(9, 10**9))
print('{0:>3} {1:>16}'.format(10, 10**10))
````



