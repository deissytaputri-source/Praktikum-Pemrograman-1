nilai = int(input())

if nilai == 0:
    hasil = "Nol"
elif nilai < 10:
    hasil = "Satuan"
elif nilai < 20:
    hasil = "Belasan"
elif nilai < 100:
    hasil = "Puluhan"
else:
    hasil = "Anda Menginput Melebihi Limit Bilangan"

print(hasil)
