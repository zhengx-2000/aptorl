#include<stdio.h>

int main()
{
    int loops = 5000;
    for(int i = 0; i < loops; i ++)
    {
        for(int j = 0; j <=i; j++)
        {
            long input1 = 1234;
            long input2 = 6789;
            long a = input1 + input2;
            long b = input1 - input2;
            long c = input1 * input2;
            long d = input1 / input2;
        }
    }
    return 0;
}
