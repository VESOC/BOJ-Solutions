#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main()
{
    int n, tmp;
    stack<int> st;
    string cmd;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        cin >> cmd;
        if (cmd == "push")
        {
            scanf("%d", &tmp);
            st.push(tmp);
        }
        else if (cmd == "top")
        {
            printf("%d\n", st.top());
        }
        else if (cmd == "pop")
        {
            if (st.size())
            {
                printf("%d\n", st.top());
                st.pop();
            }
            else
            {
                printf("-1\n");
            }
        }
        else if (cmd == "size")
        {
            int t = st.size();
            printf("%d\n", t);
        }
        else
        {
            if (st.size())
            {
                printf("0\n");
            }
            else
            {
                printf("1\n");
            }
        }
    }
}