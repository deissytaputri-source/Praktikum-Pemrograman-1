#include <stdio.h>

int main() {
    int n, kelipatan;
    scanf("%d %d", &n, &kelipatan);

    int total_semua = 0;

    for (int i = 1; i <= n; i++) {
        int total_baris = 0;

        for (int j = i; j >= 1; j--) {
            printf("(%d * %d)", j, kelipatan);
            total_baris += j * kelipatan;
            if (j != 1) {
                printf(" + ");
            }
        }

        printf(" = %d\n", total_baris);
        total_semua += total_baris;
    }

    printf("%d\n", total_semua);

    return 0;
}
