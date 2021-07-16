#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main()
{
    string s;
    cin >> s;
    stack<char> op;
    for (const auto &c : s)
    {
        if (c >= 'A' && c <= 'Z')
        {
            printf("%c", c);
        }
        else
        {
            switch (c)
            {
            case '+':
            case '-':
                while (!op.empty() && op.top() != '(')
                {
                    printf("%c", op.top());
                    op.pop();
                }
                op.push(c);
                break;

            case '*':
            case '/':
                while (!op.empty() && (op.top() == '*' || op.top() == '/'))
                {
                    printf("%c", op.top());
                    op.pop();
                }
                op.push(c);
                break;

            case '(':
                op.push(c);
                break;

            case ')':
                while (!op.empty() && op.top() != '(')
                {
                    printf("%c", op.top());
                    op.pop();
                }
                op.pop();
                break;
            }
        }
    }
    while (!op.empty())
    {
        printf("%c", op.top());
        op.pop();
    }
}