#include <iostream>
using namespace std;

int dp[11] = {
    0,
};

int getAmtNumberNeeded(int n)
{
    if (dp[n])
        return dp[n];
    return dp[n] = getAmtNumberNeeded(n - 1) + getAmtNumberNeeded(n - 2) + getAmtNumberNeeded(n - 3);
}

int main()
{
    int t, n;
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;
    cin >> t;
    while (t--)
    {
        cin >> n;
        printf("%d\n", getAmtNumberNeeded(n));
    }
}