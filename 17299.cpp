#include <iostream>
#include <stack>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    stack<int> st;
    scanf("%d", &n);
    vector<int> v(n), M(1000001, 0);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &v[i]);
        M[v[i]]++;
    }
    vector<int> ans;
    for (int i = n - 1; i >= 0; i--)
    {
        if (!st.empty())
        {
            while (!st.empty() && M[st.top()] <= M[v[i]])
                st.pop();
            if (!st.empty())
                ans.push_back(st.top());
            else
                ans.push_back(-1);
        }
        else
            ans.push_back(-1);
        st.push(v[i]);
    }
    for (int i = n - 1; i >= 0; i--)
        printf("%d ", ans[i]);
}
