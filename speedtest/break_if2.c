int main()
{
    int N = 1000;
    int a[1000];
    for(int i = 0; i < 100; i++)
    {
        a[i] += 5;
    }
    for(int i = 100; i < 200; i++)
    {
        a[i] += 10;
    }
    for(int i = 200; i < N; i++)
    {
        a[i] += 20;
    }
    // printf("%d", a[3] + a[33] + a[333]);
    return 0;
}