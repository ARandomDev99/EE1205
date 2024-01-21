#include <stdio.h>
#include <stdlib.h>

// Function that calculates x(n) = (30 * 2^n)u(n)
unsigned long long x(int n) {
    if (n < 0) {
        // 0 for all negative values
        return 0;
    }
    // 2^n can be represented as a left bitshift by n bits.
    return 30 * (1ull << n);
}

int main() {
    // File pointer
    FILE* out;
    // Open the file.
    fopen_s(&out, "11_9_3_30cout.txt", "w");
    // Character pointer to store the formatted string.
    char* formatted_str = (char*) malloc(sizeof(char) * 128);
    for (int i = 0; i < 8; i++) {
        // Format the string.
        sprintf(formatted_str, "x(%d) = %llu\n", i, x(i));
        // Write the formatted string to the file.
        fputs(formatted_str, out);
    }
    // Close the file.
    fclose(out);
    // Free the memory allocated for the formatted string.
    free(formatted_str);
}