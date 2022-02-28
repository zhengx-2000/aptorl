#include<stdio.h>

int main()
{
    int loops = 5000;
    for(int i = 0; i < loops; i++)
    {
        for(int j = 0; j <=i; j++)
        {
            float input1 = 1234.00;
            float input2 = 6789.00;
            float a = input1 + input2;
            float b = input1 - input2;
            float c = input1 * input2;
            float d = input1 / input2;
        }
    }
    return 0;
}