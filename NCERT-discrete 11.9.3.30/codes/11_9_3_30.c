#include <stdio.h>

unsigned long long x(int n) {
    if (n < 0) {
        return 0;
    }
    return 30 * (1ull << n);
}

int main() {
    printf("This program will print all values of x(n) from n = 0 to n = 50.\n");
    for (int i = 0; i <= 50; i++) {
        printf("x(%d) = %llu\n", i, x(i));
    }
}