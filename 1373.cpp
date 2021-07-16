#include <iostream>
#include <string>
using namespace std;

string convert(string s)
{
    int val = 0, incre = 1;
    for (int i = s.length() - 1; i >= 0; i--)
    {
        val += (s[i] - '0') * incre;
        incre *= 2;
    }
    return to_string(val);
}

int main()
{
    string s, ans = "";
    cin >> s;
    int ex = s.length() % 3;
    if (ex)
    {
        ans += convert(s.substr(0, ex));
    }
    for (int i = ex; i < s.length(); i += 3)
    {
        ans += convert(s.substr(i, 3));
    }
    cout << ans;
}