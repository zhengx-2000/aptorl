#include <stdio.h>
int Img[2073600] = {};
int *pTemp = Img;
int sum = 0;
int main(void)
{
    for(int i = 0; i < 1920*1080; i++)
    {
        Img[i] = i;
    }
    for(int i = 0; i < 1920; i++)
    {
        for(int j = 0; j < 1080; j++)
        {
            sum *= Img[i * 1080 + j];
        }
    }
    //printf("%d\n", sum);
    return 0;
}
