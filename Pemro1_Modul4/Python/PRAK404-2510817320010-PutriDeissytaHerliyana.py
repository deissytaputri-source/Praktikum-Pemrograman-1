while True:
    print("Pilih program")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Exit")

    pilihan = int(input("Masukkan Pilihan : "))

    if pilihan == 5:
        print("Terimakasih, telah menggunakan kalkulator PUTRI DEISSYTA HERLIYANA")
        break
    elif pilihan >= 1 and pilihan <= 4:
        nilai1 = float(input("Masukkan nilai pertama : "))
        nilai2 = float(input("Masukkan nilai kedua : "))

        if pilihan == 1:
            hasil = nilai1 + nilai2
            operasi = "Penjumlahan"
        elif pilihan == 2:
            hasil = nilai1 - nilai2
            operasi = "Pengurangan"
        elif pilihan == 3:
            hasil = nilai1 * nilai2
            operasi = "Perkalian"
        elif pilihan == 4:
            if nilai2 == 0:
                print("Error: Pembagian dengan nol tidak diperbolehkan.")
                continue
            hasil = nilai1 / nilai2
            operasi = "Pembagian"

        print(f"Hasil {operasi} antara {nilai1:.2f} dengan {nilai2:.2f} adalah {hasil:.2f}")
        print()
    else:
        print("Input anda salah, silahkan coba lagi\n")