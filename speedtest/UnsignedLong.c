#include<stdio.h>

int main()
{
    int loops = 5000;
    for(int i = 0; i < loops; i ++)
    {
        for(int j = 0; j <=i; j++)
        {
            unsigned long input1 = 1234;
            unsigned long input2 = 6789;
            unsigned long a = input1 + input2;
            unsigned long b = input1 - input2;
            unsigned long c = input1 * input2;
            unsigned long d = input1 / input2;
        }
    }
    return 0;
}
