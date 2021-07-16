#include <iostream>
using namespace std;

int main()
{
    long long pinary[91];
    int n;
    scanf("%d", &n);
    pinary[1] = 1;
    pinary[2] = 1;
    for (int i = 3; i <= n; i++)
    {
        pinary[i] = pinary[i - 1] + pinary[i - 2];
    }
    printf("%lld", pinary[n]);
}

// 처음 풀었던 방법
#include <iostream>
using namespace std;

int main()
{
    long long pinary[91][2] = {
        0,
    };
    int n;
    scanf("%d", &n);
    pinary[1][1] = 1;
    pinary[2][1] = 0;
    pinary[2][0] = 1;
    for (int i = 3; i <= n; i++)
    {
        pinary[i][0] = pinary[i - 1][0] + pinary[i - 1][1];
        pinary[i][1] = pinary[i - 1][0];
    }
    printf("%lld", pinary[n][0] + pinary[n][1]);
}