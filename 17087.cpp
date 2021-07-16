#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

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
    int n, s;
    scanf("%d %d", &n, &s);
    vector<int> v(n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &v[i]);
    }
    int ans = n > 1 ? gcd(abs(v[0] - s), abs(v[1] - s)) : abs(v[0] - s);
    for (int i = 2; i < n; i++)
    {
        ans = gcd(ans, abs(v[i] - s));
    }
    printf("%d", ans);
}