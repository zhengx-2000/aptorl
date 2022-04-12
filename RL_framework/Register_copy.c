#include <stdio.h>
// change: using register before int.
int main(){
    register int n = 10000, sum = 0;
    // using register variables
    // as counters make the loop faster
    for (register int i = 0; i < n; ++i) {
        for (register int j = 0; j <= i; ++j) {
            sum += i + j;
        }
    }
    printf("%d", sum);
    return 0;
}
