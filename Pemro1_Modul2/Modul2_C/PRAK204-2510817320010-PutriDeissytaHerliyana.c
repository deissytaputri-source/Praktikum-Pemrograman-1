#include <stdio.h>

int main() {
    float r, t;
    float volume, luas, keliling;
    float pi = 22.0 / 7.0;

    scanf("%f %f", &r, &t);

    volume = pi * r * r * t;             
    luas = 2 * pi * r * (r + t);       
    keliling = 2 * pi * r;             

    printf("Volume = %.2f\n", volume);
    printf("Luas = %.2f\n", luas);
    printf("Keliling = %.2f\n", keliling);

    return 0;
}
