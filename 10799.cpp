#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main()
{
    string s;
    cin >> s;
    int pieces = 0, i = 0;
    stack<char> st;

    while (i < s.size())
    {
        if (s[i] == '(')
        {
            if (s[i + 1] == ')')
            {
                pieces += st.size();
                i += 2;
            }
            else
            {
                st.push('(');
                pieces++;
                i++;
            }
        }
        else
        {
            if (!st.empty())
                st.pop();
            i++;
        }
    }

    printf("%d", pieces);
}