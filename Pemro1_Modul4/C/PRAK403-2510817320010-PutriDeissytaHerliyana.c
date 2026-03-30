#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);

    if (a < b) {
        for (int i = a, j = b; i <= b && j >= a; i++, j--) {
            printf("%d %d", i, j);
            if (i != b && j != a)
                printf(" - ");
        }
    } else {
        for (int i = a, j = b; i >= b && j <= a; i--, j++) {
            printf("%d %d", i, j);
            if (i != b && j != a)
                printf(" - ");
        }
    }

    printf("\n");
    return 0;
}
