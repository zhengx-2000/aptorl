#include<stdio.h>

int main()
{
    int loops = 5000;
    for(int i = 0; i < loops; i ++)
    {
        for(int j = 0; j <=i; j++)
        {
            short input1 = 1234;
            short input2 = 6789;
            short a = input1 + input2;
            short b = input1 - input2;
            short c = input1 * input2;
            short d = input1 / input2;
        }
    }
    return 0;
}
