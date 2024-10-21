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
  if bilangan ==0:
      break
  if bilangan > bilangan_terbesar:
       bilangan_terbesar = bilangan

  if bilangan_terbesar == float('-inf'):
       print("tidak ada bilangan yang di masukkan.")
  else:
      print("Bilangan terbesar adalah:", bilangan_terbesar) )
````

    
  Masukkan bilangan (tekan 0 untuk berhenti): 80
  
  Masukkan bilangan (tekan 0 untuk berhenti): 60
  
  Masukkan bilangan (tekan 0 untuk berhenti): 20
  
  Masukkan bilangan (tekan 0 untuk berhenti): 0
  
  Bilangan terbesar adalah : 80.0

# Berikut Hasil di Visual Studio Code

   ![Screenshot (11)](https://github.com/user-attachments/assets/702d0721-8f48-41a3-9598-3f08358e0401)











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
   
  ![Screenshot (12)](https://github.com/user-attachments/assets/6fd42b73-fb26-4f66-8574-84ded7b186c0)









# Berikut adalah Flowchartnya

 ![Untitled Diagram drawio](https://github.com/user-attachments/assets/e1bc1c5b-3006-49b8-b99c-278696291cf9)
















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

![Screenshot (15)](https://github.com/user-attachments/assets/82e535ce-fe7c-4980-8a82-760dc606484f)






``` PYTHON
(#Penggunaan end
   print('A', end='')
   print('B', end='')
   print('C', end='')
   print()
   print('X')
   print('Y')
   print('Z')

 #Pengunaan Separator
   w, x, y, z = 10, 15, 20, 25
   print(w, x, y, z)
   print(w, x, y, z, sep=',')
   print(w, x, y, z, sep='')
   print(w, x, y, z, sep=':')
   print(w, x, y, z, sep='-----')
````

Parameter end dalam fungsi Print() di Python di gunakan untuk menambahkan string("")apapun diakhiri dan mengeluarkan pertanyaan print

Print()

secara default, fungsi Print() akan mengakhiri dengan baris baru, dan akan secra otomatis karakter baris baru di akhir outputnya.


berikut hasil screenshot dari pemrograman Penggunaan END

   ![WhatsApp Image 2024-10-21 at 07 57 20 (2)](https://github.com/user-attachments/assets/0522fa82-f7fb-410d-806d-d8dfa656f907)

   

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

print('{0:>3} {1:>16}'.format(0, 10**0)
print('{0:>3} {1:>16}'.format(1, 10**1)
print('{0:>3} {1:>16}'.format(2, 10**2)
print('{0:>3} {1:>16}'.format(3, 10**3)
print('{0:>3} {1:>16}'.format(4, 10**4)
print('{0:>3} {1:>16}'.format(5, 10**5)
print('{0:>3} {1:>16}'.format(6, 10**6)
print('{0:>3} {1:>16}'.format(7, 10**7)
print('{0:>3} {1:>16}'.format(8, 10**8)
print('{0:>3} {1:>16};.format(9, 10**9)
print('{0:>3} {1:>16}'.format(10, 10**10)
````

string format adalah proses memasukkan variable atau string kustom kedalam teks yang sudah ditentukan dan dapar digunakan untuk berbagi keperluan, seperti memasukkan judul dalam grafik menampilkan pesan atau kesalahan kesuatu fungsi

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
````
Nilai pertama dalam setiap pasangan adalah angka dari 0 hingga 10, kode programan ini dihitung dengan menggunakan operasi pangkat atau fungsinya (**) untuk menaikkan 10 kepangkat yang sesuai dengan angka pertama yang bisa dibahasa manusiakan variable 0 = 10 pangkat 0, variable 1 10 pangkat 1 dan seterusnya hingga variable 10 yaitu 10 pangkat 10, dan dicetak dengan fungsi print()

```PYTHON
print('{0:>3} {1:>16}'.format(0, 10**0)
print('{0:>3} {1:>16}'.format(1, 10**1)
print('{0:>3} {1:>16}'.format(2, 10**2)
print('{0:>3} {1:>16}'.format(3, 10**3)
print('{0:>3} {1:>16}'.format(4, 10**4)
print('{0:>3} {1:>16}'.format(5, 10**5)
print('{0:>3} {1:>16}'.format(6, 10**6)
print('{0:>3} {1:>16}'.format(7, 10**7)
print('{0:>3} {1:>16}'.format(8, 10**8)
print('{0:>3} {1:>16};.format(9, 10**9)
print('{0:>3} {1:>16}'.format(10, 10**10)
````
Kode ini mencetak 11 baris dengan format {0:3} {1:16} yang digunakan untuk mengatur format string.
pada string pertama, angka 0 diformat untuk memiliki lebar 3 karakter atau yang bisa disebut 3 kali spasi dengan perataan kanan. angka 1 di format untuk memiliki lebar 16 karakter atau 16 kali spasi dengan perataan kanan, dan masing-masing mencetak nilai seperti format diatas dengan fungsi print().
