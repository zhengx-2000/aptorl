#include <stdio.h>
int main() {
    int x=2;
    for(int i=0; i<2500; i++) {
        x*=x;
    }
    for(int j=2501; j<5000; j++) {
        x*=x;
    }
    for(int k=5001; k<7500; k++) {
        x*=x;
    }
    for(int l=7501; l<10000; l++) {
        x*=x;
    }
    return 0;
}
