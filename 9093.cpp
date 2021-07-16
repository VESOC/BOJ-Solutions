#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main()
{
    int n;
    string s;
    stack<char> st;

    cin >> n;
    cin.ignore();
    while (n--)
    {
        getline(cin, s);
        s += ' ';

        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] == ' ')
            {
                while (!st.empty())
                {
                    cout << st.top();
                    st.pop();
                }
                cout << ' ';
            }
            else
                st.push(s[i]);
        }
        cout << "\n";
    }
}