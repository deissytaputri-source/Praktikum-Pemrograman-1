n, kelipatan = map(int, input().split())

total_semua = 0

for i in range(1, n + 1):
    total_baris = 0

    for j in range(i, 0, -1):
        print(f"({j} * {kelipatan})", end="")
        total_baris += j * kelipatan
        if j != 1:
            print(" + ", end="")
    print(f" = {total_baris}")
    total_semua += total_baris

print(total_semua)
