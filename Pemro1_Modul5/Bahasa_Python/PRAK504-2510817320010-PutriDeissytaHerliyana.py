def reverse(x):
    hasil = 0
    while x > 0:
        hasil = hasil * 10 + (x % 10)
        x //= 10
    return hasil

A, B = map(int, input().split())

A = reverse(A)
B = reverse(B)

C = A + B
print(reverse(C))
