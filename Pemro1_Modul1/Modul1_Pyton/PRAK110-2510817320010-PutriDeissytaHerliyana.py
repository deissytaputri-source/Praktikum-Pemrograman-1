alas = 5
tinggi = 12

sisimiring = (alas**2 + tinggi**2) ** 0.5

keliling = alas + tinggi + sisimiring
luas = (alas * tinggi) / 2

print("Diketahui :")
print("Alas =", alas, "cm")
print("Tinggi =", tinggi, "cm")

print("\nJawab :")
print(f"Sisi A = {alas:.0f} cm")
print(f"Sisi B = {tinggi:.0f} cm")
print(f"Sisi C = {sisimiring:.0f} cm")
print(f"Keliling = {keliling:.0f} cm")
print(f"Luas = {luas:.0f} cm")