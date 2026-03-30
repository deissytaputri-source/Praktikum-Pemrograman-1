def MaxBilangan(a, b, c, d):
    terbesar = a
    if b > terbesar:
        terbesar = b
    if c > terbesar:
        terbesar = c
    if d > terbesar:
        terbesar = d
    return terbesar

a, b, c, d = map(int, input().split())

hasil = MaxBilangan(a, b, c, d)
print(hasil)
