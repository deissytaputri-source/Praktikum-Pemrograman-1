import math

A, B = map(float, input().split())

C = math.sqrt(B*B - A*A)  

keliling = A + B + C
luas = 0.5 * A * C

print(f"Alas = {C:.0f} cm")
print(f"Tinggi = {A:.0f} cm")
print(f"Keliling = {keliling:.0f} cm")
print(f"Luas = {luas:.0f} cm^2")
