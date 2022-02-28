#include <stdio.h>
int Img[2073600] = {};
int sum = 0;
int *pTemp = Img;
int main(void)
{
    for(int i = 0; i < 1920*1080; i++)
    {
        Img[i] = i;
    }
    for(int i = 0; i < 1920; i++, pTemp += 1080)
    {
        for(int j = 0; j < 1080; j++)
        {
            sum *= pTemp[j];
        }
    }
    //printf("%d\n", sum);
    return 0;
}
