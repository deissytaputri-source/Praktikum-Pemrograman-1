#include <stdio.h>

int main() {
    int input;
    scanf("%d", &input);

    int hari = 0, jam = 0, menit = 0, detik = 0;

    hari = input / 86400;            // 1 hari = 86400 detik
    jam = (input % 86400) / 3600;    // sisa hari dibagi 3600 detik = jam
    menit = (input % 3600) / 60;     // sisa jam dibagi 60 detik = menit
    detik = input % 60;              // sisa terakhir = detik

    if (hari == 0) {
        printf("%.2d:%.2d:%.2d\n", jam, menit, detik);
    } else {
        printf("%d hari %.2d:%.2d:%.2d\n", hari, jam, menit, detik);
    }

    return 0;
}
