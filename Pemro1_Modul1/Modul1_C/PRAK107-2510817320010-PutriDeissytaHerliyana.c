#include <stdio.h>

int main() {
    int sisi1 = 4;
    int sisi2 = 5;
    int sisi3 = 7;
    int keliling = sisi1 + sisi2 + sisi3;
    int hargapermeter = 85000;
    int totalbiaya = keliling * hargapermeter;

    printf("Diketahui : \n");
    printf("Panjang sisi segitiga berturut-berturut adalah %d, %d, dan %d \n", sisi1, sisi2, sisi3);
    printf("Keliling Tanah Pak Dengklek adalah %d \n", keliling);
    printf("Harga tanah Per Meter adalah %d\n", hargapermeter);
    printf("Jawaban : \n");
    printf("Biaya yang diperlukan Pak Dengklek adalah : Rp %d\n", totalbiaya);

    return 0;

}