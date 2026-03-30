#include <stdio.h>

int main(){
    int nilai;

    scanf("%d", &nilai);

    if(nilai==0){
        printf("nol\n");
    } else if(nilai > 0){
        printf("positif\n");
    } else{
        printf("negatif\n");
    }

    return 0;
}