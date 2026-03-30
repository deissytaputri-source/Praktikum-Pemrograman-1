#include <stdio.h>

int main() {
    int a = 4;
    int b = 8;
    int c = 3;

    float kombinasi = (float) (a * b) / c;

    printf("Variabel a bernilai %d\n", a);
    printf("Variabel b bernilai %d\n", b);
    printf("Variabel c bernilai %d\n", c);
    printf("Hasil dari a dikali b dibagi c adalah %.6f\n", kombinasi);

    return 0;
}