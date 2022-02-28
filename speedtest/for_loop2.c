#include <stdio.h>
int main() {
    int x=2;
    for(int i=10000; i>0; i--) {
        x*=x;
    }
    return 0;
}
