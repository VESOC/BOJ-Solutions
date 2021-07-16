#include <iostream>
#define DM 1000000000
using namespace std;

int main()
{
    int stepNumber[101][11] = {
        0,
    };
    for (int i = 1; i < 10; i++)
    {
        stepNumber[1][i] = 1;
    }
    int n;
    scanf("%d", &n);
    for (int i = 2; i <= n; i++)
    {
        stepNumber[i][0] = stepNumber[i - 1][1];
        for (int j = 1; j < 10; j++)
        {
            stepNumber[i][j] = (stepNumber[i - 1][j - 1] + stepNumber[i - 1][j + 1]) % DM;
        }
    }
    long long ans = 0;
    for (int i = 0; i < 10; i++)
    {
        ans += stepNumber[n][i];
    }
    cout << ans % DM;
}
// Sliding Window 기법
#include <iostream>
#define MOD 1000000000
using namespace std;

int a[2][12];

int main()
{
    int n, ans = 9;
    scanf("%d", &n);
    for (int i = 2; i < 11; i++)
        a[1][i] = 1;
    for (int i = 2; i <= n; i++)
    {
        ans = 0;
        for (int j = 1; j < 11; j++)
        {
            a[i % 2][j] = (a[(i - 1) % 2][j - 1] + a[(i - 1) % 2][j + 1]) % MOD;
            ans = (ans + a[i % 2][j]) % MOD;
        }
    }
    printf("%d", ans);
}