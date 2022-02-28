#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    int n = 10, sum;
    // using register variables
    // as counters make the loop faster
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j <= i; ++j) {
            sum += i + j;
            //printf("%d ",i + j);
        }
    }
    printf("%d\n", sum);
    return 0;
}
