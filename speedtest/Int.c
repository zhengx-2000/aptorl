#include<stdio.h>

int main()
{
    int loops = 5000;
    for(int i = 0; i < loops; i ++)
    {
        for(int j = 0; j <=i; j++)
        {
            int input1 = 1234;
            int input2 = 6789;
            int a = input1 + input2;
            int b = input1 - input2;
            int c = input1 * input2;
            int d = input1 / input2;
        }
    }
    return 0;
}
