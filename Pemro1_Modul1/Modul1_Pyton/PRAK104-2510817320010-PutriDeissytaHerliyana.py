a = 400000
b = 350000

diskona = 13 / 100
diskonb = 21 / 100

hargaakhira = a - (a * diskona)
hargaakhirb = b - (b * diskonb)

print("Harga sepatu a adalah", a)
print("Harga sepatu b adalah", b)
print("Sepatu A mendapatkan diskon 13% sehingga harganya menjadi", int(hargaakhira))
print("Sepatu B mendapatkan diskon 21% sehingga harganya menjadi", int(hargaakhirb))