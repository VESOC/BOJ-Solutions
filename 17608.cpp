#include <iostream>
using namespace std;

int main()
{
    int rods[100001], n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &rods[i]);
    }
    int max = rods[n - 1], cnt = 1;
    for (int i = n - 2; i >= 0; i--)
    {
        if (max < rods[i])
        {
            max = rods[i];
            cnt++;
        }
    }
    printf("%d\n", cnt);
}