#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string convert(char s)
{
    int n = s - '0';
    string ans = "";
    if (n == 0)
    {
        return "0";
    }
    while (n > 0)
    {
        ans += to_string(n % 2);
        n /= 2;
    }
    reverse(ans.begin(), ans.end());
    return ans;
}

int main()
{
    string s, ans = "", tmp;
    cin >> s;
    if (s[0] == '0')
    {
        printf("0");
        return 0;
    }
    for (int i = 0; i < s.length(); i++)
    {
        if (i == 0)
        {
            ans += convert(s[i]);
        }
        else
        {
            tmp = convert(s[i]);
            while (tmp.length() < 3)
            {
                tmp = "0" + tmp;
            }
            ans += tmp;
        }
    }
    cout << ans;
}