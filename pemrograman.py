bilangan_terbesar = float('-inf')  

while True:
    bilangan = float(input("Masukkan bilangan (tekan 0 untuk berhenti): "))
    if bilangan == 0:
        break   
    if bilangan > bilangan_terbesar:
        bilangan_terbesar = bilangan

if bilangan_terbesar == float('-inf'):
    print("Tidak ada bilangan yang dimasukkan.")
else:
    print("Bilangan terbesar adalah:", bilangan_terbesar)