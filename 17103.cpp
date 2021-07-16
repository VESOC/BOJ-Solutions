#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n = 1000001;
    int arr[n];
    fill_n(arr, n, 1);
    arr[0] = 0;
    arr[1] = 0;
    for (int i = 2; i < n; i++)
    {
        if (arr[i])
        {
            for (int j = i + i; j < n; j += i)
            {
                arr[j] = 0;
            }
        }
    }
    int t, val;
    cin >> t;
    while (t--)
    {
        int cnt = 0;
        cin >> val;
        for (int i = 2; i <= val / 2; i++)
        {
            if (arr[i] && arr[val - i])
            {
                cnt++;
            }
        }
        cout << cnt << '\n';
    }
}