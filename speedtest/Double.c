#include<stdio.h>

int main()
{
    int loops = 5000;
    for(int i = 0; i < loops; i ++)
    {
        for(int j = 0; j <=i; j++)
        {
            double input1 = 1234.00;
            double input2 = 6789.00;
            double a = input1 + input2;
            double b = input1 - input2;
            double c = input1 * input2;
            double d = input1 / input2;
        }
    }
    return 0;
}