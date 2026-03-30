nilai = int(input())

if nilai >= 80:
    huruf = "A"
elif 70 <= nilai <= 79:
    huruf = "B"
elif 60 <= nilai <= 69:
    huruf = "C"
elif 50 <= nilai <= 59:
    huruf = "D"
else:
    huruf = "E"

print(huruf)
