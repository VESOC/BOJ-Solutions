#include <iostream>
#include <stack>
using namespace std;

int main()
{
    int n, num, cur = 1;
    stack<int> s;
    string ans = "";
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &num);
        if (num >= cur)
        {
            while (num + 1 != cur)
            {
                s.push(cur++);
                ans += "+\n";
            }
            s.pop();
            ans += "-\n";
        }
        else
        {
            if (s.top() == num)
            {
                s.pop();
                ans += "-\n";
            }
            else
            {
                ans = "NO";
                break;
            }
        }
    }
    cout << ans;

    return 0;
}