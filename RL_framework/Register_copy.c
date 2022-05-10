#include <stdio.h>
// change: using register before int.
int main(){
    int n = 10000, sum = 0;
    // using register variables
    // as counters make the loop faster
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j <= i; ++j) {
            sum += i + j;
        }
    }
    printf("%d", sum);
    return 0;
}
