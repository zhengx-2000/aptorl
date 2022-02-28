#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int n = 10000;
    register int i = 0;
    register int j = 0;
    // using register variables
    // as counters make the loop faster
    for (i = 0; i < n; ++i)
    {
        for (j = 0; j <= i; ++j)
        {
            //printf("%d" ,i + j);
        }
    }
    return 0;
}