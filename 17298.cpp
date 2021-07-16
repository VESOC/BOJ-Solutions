#include <iostream>
#include <stack>
#include <vector>
#include <utility>
using namespace std;

int main()
{
    int n, tmp;
    stack<pair<int, int>> st;
    scanf("%d", &n);
    vector<int> l(n);
    for (int i = 0; i < n; i++)
    {
        l[i] = -1;
    }
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &tmp);
        if (st.empty())
            st.push(make_pair(tmp, i));
        else
        {
            if (tmp > st.top().first)
            {
                while (!st.empty())
                {
                    if (st.top().first < tmp)
                    {
                        l[st.top().second] = tmp;
                        st.pop();
                    }
                    else
                    {
                        break;
                    }
                }
            }
            st.push(make_pair(tmp, i));
        }
    }
    for (int i = 0; i < n; i++)
        printf("%d ", l[i]);
}

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <stack>
using namespace std;

int main()
{
    int n;
    int num;
    vector<int> v;
    stack<int> s;

    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &num);
        v.push_back(num);
    }

    vector<int> ans(v.size(), -1);

    for (int i = 0; i < v.size(); i++)
    {
        while (!s.empty() && v[s.top()] < v[i])
        {
            ans[s.top()] = v[i];
            s.pop();
        }
        s.push(i);
    }

    for (int x : ans)
    {
        cout << x << " ";
    }

    return 0;
}