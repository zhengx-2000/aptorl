int main()
{
    int N = 1000;
    int a[1000];
    for(int i = 0; i < N; i++)
    {
        if(i < 100) a[i] += 5;
        else if(i < 200) a[i] += 10;
        else a[i] += 20;
    }
    // printf("%d", a[3] + a[33] + a[333]);
    return 0;
}