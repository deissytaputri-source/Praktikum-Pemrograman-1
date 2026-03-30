input_detik = int(input())

hari = input_detik // 86400
jam = (input_detik % 86400) // 3600
menit = (input_detik % 3600) // 60
detik = input_detik % 60

if hari == 0:
    print(f"{jam:02d}:{menit:02d}:{detik:02d}")
else:
    print(f"{hari} hari {jam:02d}:{menit:02d}:{detik:02d}")
