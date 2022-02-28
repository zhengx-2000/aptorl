#include <stdio.h>
int main() {
    int x=2;
    for(int i=0; i<10000; i++) {
        x*=x;
    }
    return 0;
}
