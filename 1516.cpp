#include <bits/stdc++.h>
using namespace std;

#define MAX 501

int connected[MAX], t[MAX], result[MAX];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int n;
    cin >> n;
    vector<int> need[MAX];
    for (int i = 1;i <= n;i++) {
        int x;
        cin >> t[i];
        while (true) {
            cin >> x;
            if (x == -1) break;
            need[x].push_back(i);
            connected[i]++;
        }
    }
    queue<int> q;
    for (int i = 1;i <= n;i++) {
        if (connected[i] == 0) {
            q.push(i);
            result[i] = t[i];
        }
    }
    for (int i = 1;i <= n;i++) {
        int x = q.front();
        q.pop();
        for (int j = 0;j < need[x].size();j++) {
            int y = need[x][j];
            result[y] = max(result[y], result[x] + t[y]);
            if (--connected[y] == 0) q.push(y);
        }
    }
    for (int i = 1;i <= n;i++) {
        cout << result[i] << '\n';
    }
}