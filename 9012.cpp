#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main()
{
    int n;
    string s, ans = "";
    stack<char> st;
    cin >> n;
    while (n--)
    {
        cin >> s;
        stack<char> st;
        for (const char &c : s)
        {
            if (c == '(')
            {
                st.push(c);
            }
            else
            {
                if (!st.empty())
                {
                    st.pop();
                }
                else
                {
                    st.push('(');
                    break;
                }
            }
        }
        if (!st.empty())
        {
            ans += "NO\n";
        }
        else
        {
            ans += "YES\n";
        }
    }
    cout << ans;
}