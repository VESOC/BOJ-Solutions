#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int m, n;
    cin >> m >> n;
    vector<int> v(n + 1, 1);
    v[0] = 0;
    v[1] = 0;
    for (int i = 2; i <= n; i++)
    {
        if (v[i])
        {
            for (int j = i + i; j <= n; j += i)
            {
                v[j] = 0;
            }
        }
    }
    for (int i = m; i <= n; i++)
    {
        if (v[i])
        {
            cout << i << '\n';
        }
    }
}