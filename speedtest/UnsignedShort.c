#include<stdio.h>

int main()
{
    int loops = 5000;
    for(int i = 0; i < loops; i ++)
    {
        for(int j = 0; j <=i; j++)
        {
            unsigned short input1 = 1234;
            unsigned short input2 = 6789;
            unsigned short a = input1 + input2;
            unsigned short b = input1 - input2;
            unsigned short c = input1 * input2;
            unsigned short d = input1 / input2;
        }
    }
    return 0;
}
