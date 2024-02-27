#ifndef EE1205_EE1205_H
#define EE1205_EE1205_H

#include <stdlib.h>

// Does the same thing as Python's numpy.linspace(...)
double* linspace(double start, double stop, size_t count) {
    double* result = (double*) malloc(sizeof(double) * count);
    result[0] = start;
    result[count - 1] = stop;
    for (size_t i = 1; i < count - 1; i++) {
        result[i] = start + (stop - start) * i / count;
    }
    return result;
}

#endif
