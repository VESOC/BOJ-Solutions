#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    string s;
    int ans[26];
    fill_n(ans, 26, -1);
    cin >> s;
    for (int i = 0; i < s.length(); i++)
    {
        if (ans[s[i] - 'a'] == -1)
        {
            ans[s[i] - 'a'] = i;
        }
    }
    for (const int &v : ans)
    {
        printf("%d ", v);
    }
}