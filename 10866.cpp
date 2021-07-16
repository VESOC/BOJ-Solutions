#include <iostream>
#include <deque>
using namespace std;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int n, tmp;
    deque<int> dq;
    string op;
    cin >> n;

    while (n--)
    {
        cin >> op;
        if (op == "push_front")
        {
            cin >> tmp;
            dq.push_front(tmp);
        }
        else if (op == "push_back")
        {
            cin >> tmp;
            dq.push_back(tmp);
        }
        else if (op == "pop_front")
        {
            if (dq.empty()) cout << -1 << '\n';
            else
            {
                cout << dq.front() << '\n';
                dq.pop_front();
            }
        }
        else if (op == "pop_back")
        {
            if (dq.empty()) cout << -1 << '\n';
            else
            {
                cout << dq.back() << '\n';
                dq.pop_back();
            }
        }
        else if (op == "size")
        {
            cout << dq.size() << '\n';
        }
        else if (op == "empty")
        {
            cout << dq.empty() << '\n';
        }
        else if (op == "front")
        {
            if (dq.empty()) cout << -1 << '\n';
            else cout << dq.front() << '\n';
        }
        else if (op == "back")
        {
            if (dq.empty()) cout << -1 << '\n';
            else cout << dq.back() << '\n';
        }
    }

    return 0;
}