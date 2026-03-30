#include <stdio.h>

int main() {
    int nilai;
    scanf("%d", &nilai);

    char huruf;

    if (nilai >= 80) {
        huruf = 'A';
    } else if (nilai >= 70 && nilai <= 79) {
        huruf = 'B';
    } else if (nilai >= 60 && nilai <= 69) {
        huruf = 'C';
    } else if (nilai >= 50 && nilai <= 59) {
        huruf = 'D';
    } else {
        huruf = 'E';
    }

    printf("%c\n", huruf);
    return 0;
}
