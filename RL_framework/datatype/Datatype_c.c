#include <stdio.h>
#include <math.h>
#define n 5000
// change: using different datatypes.
int main(){
    int sum = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j <= i; ++j) {
            sum += pow(-1, i + j);
        }
    }
    printf("%d", sum);
    return 0;
}