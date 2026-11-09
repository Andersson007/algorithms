#include "stdio.h"
#include "stddef.h"

int main(void) {
    int a[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    for (size_t i = 0; i < sizeof(a) / sizeof(a[0]); i++) {
        printf("%d\n", a[i]);
    }
}
