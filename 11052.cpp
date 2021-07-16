#include <iostream>
#include <cmath>
using namespace std;

int dp[1001];

int main()
{
    int n, tmp, p[1001], dp[1001];
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
        scanf("%d", &tmp);
        p[i] = tmp;
        dp[i] = tmp;
    }
    for (int i = 2; i <= n; i++)
    {
        for (int j = 1; j < i; j++)
        {
            dp[i] = max(p[j] + dp[i - j], dp[i]);
        }
    }
    printf("%d\n", dp[n]);
}