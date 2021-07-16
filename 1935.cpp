#include <iostream>
#include <string>
#include <stack>
#include <vector>
using namespace std;

int main()
{
    int n;
    stack<double> st;
    string s;
    scanf("%d", &n);
    cin >> s;
    vector<double> v(n);
    for (int i = 0; i < n; i++)
        scanf("%lf", &v[i]);
    for (const char &c : s)
    {
        if (c == '+' || c == '-' || c == '*' || c == '/')
        {
            double a = st.top();
            st.pop();
            double b = st.top();
            st.pop();
            switch (c)
            {
            case '+':
                st.push(b + a);
                break;
            case '-':
                st.push(b - a);
                break;
            case '*':
                st.push(b * a);
                break;
            case '/':
                st.push(b / a);
                break;
            }
        }
        else
        {
            st.push(v[c - 'A']);
        }
    }
    printf("%.2lf", st.top());
}