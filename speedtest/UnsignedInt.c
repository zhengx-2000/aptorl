#include<stdio.h>

int main()
{
    int loops = 5000;
    for(int i = 0; i < loops; i ++)
    {
        for(int j = 0; j <=i; j++)
        {
            unsigned int input1 = 1234;
            unsigned int input2 = 6789;
            unsigned int a = input1 + input2;
            unsigned int b = input1 - input2;
            unsigned int c = input1 * input2;
            unsigned int d = input1 / input2;
        }
    }
    return 0;
}
