a, b = map(int, input().split())

if a < b:
    i, j = a, b
    while i <= b and j >= a:
        print(f"{i} {j}", end='')
        if i != b and j != a:
            print(" - ", end='')
        i += 1
        j -= 1
else:
    i, j = a, b
    while i >= b and j <= a:
        print(f"{i} {j}", end='')
        if i != b and j != a:
            print(" - ", end='')
        i -= 1
        j += 1
print()
