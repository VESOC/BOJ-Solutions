#include <iostream>
#include <queue>
#include <string>

using namespace std;
int main() {
    queue<int> q;
    string ip;
    int tmp, n;
    scanf("%d", &n);
    while (n--)
    {
        cin >> ip;
        if (ip == "pop") {
            if (!q.empty()) {
                printf("%d\n", q.front());
                q.pop();
            }
            else {
                printf("-1\n");
            }
        }
        else if (ip == "size") {
            printf("%d\n", q.size());
        }
        else if (ip == "empty") {
            if (!q.empty()) {
                printf("0\n");
            }
            else {
                printf("1\n");
            }
        }
        else if (ip == "front") {
            if (!q.empty()) {
                printf("%d\n", q.front());
            }
            else {
                printf("-1\n");
            }
        }
        else if (ip == "back") {
            if (!q.empty()) {
                printf("%d\n", q.back());
            }
            else {
                printf("-1\n");
            }
        }
        else {
            scanf("%d", &tmp);
            q.push(tmp);
        }
    }
}