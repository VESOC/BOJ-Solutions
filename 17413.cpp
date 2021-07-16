#include <stack>
#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s;
    getline(cin, s);
    stack<char> st;
    int n = 0, tmp;
    while (n < s.size())
    {
        if (s[n] == '<')
        {
            while (!st.empty())
            {
                cout << st.top();
                st.pop();
            }
            while (n < s.size())
            {
                cout << s[n];
                n++;
                if (n < s.size() && s[n] == '>')
                {
                    cout << '>';
                    n++;
                    break;
                }
            }
        }
        else if (s[n] == ' ')
        {
            while (!st.empty())
            {
                cout << st.top();
                st.pop();
            }
            cout << ' ';
            n++;
        }
        else
        {
            st.push(s[n]);
            n++;
        }
    }
    while (!st.empty())
    {
        cout << st.top();
        st.pop();
    }
}