#include <iostream>
#include <queue>
using namespace std;

int main()
{
    int n, k, tmp;
    scanf("%d %d", &n, &k);
    queue<int> q;
    for (int i = 1; i <= n; i++)
    {
        q.push(i);
    }
    printf("<");
    while (n--)
    {
        for (int i = 0; i < k - 1; i++)
        {
            q.push(q.front());
            q.pop();
        }
        printf("%d", q.front());
        q.pop();
        if (n)
            printf(", ");
    }
    printf(">");
}
