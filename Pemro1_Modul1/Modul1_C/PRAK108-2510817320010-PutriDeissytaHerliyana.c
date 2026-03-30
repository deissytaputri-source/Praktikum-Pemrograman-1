#include <stdio.h>
#define PI 3.14

int main() {
    float putaran = 5;
    float jarak = 14;
    float jarijari;

    jarijari = jarak / (putaran * 2 * PI);

    printf("Diketahui : \n");
    printf("Pak Dengklek mengelilingi taman = %.0f Putaran \n", putaran);
    printf("Jarak tempuh Pak Dengklek = %.0f Kilometer \n\n", jarak);
    
    printf("Jawaban : \n");
    printf("Jari-jari taman yang dikelilingi Pak Dengklek adalah %.2f Kilometer \n", jarijari);

    return 0;
}
