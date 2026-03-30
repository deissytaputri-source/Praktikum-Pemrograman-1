def hitung(nilai1, nilai2):
    hasil = nilai1 - nilai2
    if hasil < 0:
        hasil = -hasil
    return hasil

def mutlak(angka):
    if angka < 0:
        angka = -angka
    return angka

a, c, b, d = map(int, input().split())

hasil = hitung(a, b) + hitung(c, d)
print(mutlak(hasil))
