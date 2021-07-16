#include <iostream>
#include <vector>
using namespace std;

int arr[100];

int gcd(int x, int y)
{
    int tmp;
    if (x < y)
    {
        tmp = x;
        x = y;
        y = tmp;
    }
    while (y > 0)
    {
        tmp = x % y;
        x = y;
        y = tmp;
    }
    return x;
}

int main()
{
    int n;
    scanf("%d", &n);
    while (n--)
    {
        int c;
        long long sum = 0;
        scanf("%d", &c);
        for (int i = 0; i < c; i++)
        {
            scanf("%d", &arr[i]);
        }
        for (int i = 0; i < c; i++)
        {
            for (int j = i + 1; j < c; j++)
            {
                sum += gcd(arr[i], arr[j]);
            }
        }
        printf("%lld\n", sum);
    }
}