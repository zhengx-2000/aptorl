#include <stdio.h>

int next(int s, int *a, int n, int m){
    a[s] = 0;
    while (m--){ 
        do {
            s = (s + 1) % n;
        } while (!a[s]);
    }
    return s;
}

int main(int argc, char *argv[]){
    int n;
    int m;
    int i;
    int s;
    int a[200];
    n=23;
    for (m = 1; ; m++){
        for (i = 0; i < n; i++)
            a[i] = 1;
        s = 0;
        for (i = 0; i < n - 1; i++)
            s = next(s, a, n, m);
        if (s + 1 == 13){
            printf("%d\n", m);
            break;
        }
    }
    return 0;
}
