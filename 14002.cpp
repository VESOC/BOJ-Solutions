#include <iostream>
#include <vector>
using namespace std;

int ip[1001], t[1001], dp[1001];

void track(int p)
{
    if (p == -1)
    {
        return;
    }
    track(t[p]);
    printf("%d ", ip[p]);
}

int main()
{
    int n, max = 0, idx;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%d", &ip[i]);
    for (int i = 0; i < n; i++)
    {
        dp[i] = 1;
        t[i] = -1;
        for (int j = 0; j < i; j++)
            if (ip[i] > ip[j])
                if (dp[i] < dp[j] + 1)
                {
                    dp[i] = dp[j] + 1;
                    t[i] = j;
                }
        if (max < dp[i])
        {
            max = dp[i];
            idx = i;
        }
    }
    printf("%d\n", max);
    track(idx);
}