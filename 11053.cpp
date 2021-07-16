#include <iostream>
using namespace std;

int main()
{
    int ip[1000], n, ans = 1;
    int dp[1000] = {
        0,
    };
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &ip[i]);
    }
    for (int i = 0; i < n; i++)
    {
        int cnt = 0;
        for (int j = 0; j < i; j++)
            if (ip[i] > ip[j])
                if (cnt < dp[j])
                    cnt = dp[j];
        dp[i] = cnt + 1;
        if (ans < dp[i])
            ans = dp[i];
    }
    printf("%d", ans);
}