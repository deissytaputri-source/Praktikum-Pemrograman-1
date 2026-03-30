def maksimal(a, b):
    if a > b:
        return a
    else:
        return b

def minimal(a, b):
    if a < b:
        return a
    else:
        return b

banyak = int(input())
angka = list(map(int, input().split()))

maks = -100000
minim = 100000

for nilai in angka:
    maks = maksimal(maks, nilai)
    minim = minimal(minim, nilai)

print(maks, minim)
