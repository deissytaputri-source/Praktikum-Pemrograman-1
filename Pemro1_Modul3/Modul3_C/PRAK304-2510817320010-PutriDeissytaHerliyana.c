#include <stdio.h>

int main() {
    int nilai;
    scanf("%d", &nilai);

    if (nilai == 0) {
        printf("Nol\n");
    } else if (nilai < 10) {
        printf("Satuan\n");
    } else if (nilai < 20) {
        printf("Belasan\n");
    } else if (nilai < 100) {
        printf("Puluhan\n");
    } else {
        printf("Anda Menginput Melebihi Limit Bilangan\n");
    }

    return 0;
}
