#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int n, m;
    cin >> n >> m;
    vector<int> g(n + 1), h[n + 1];
    int result[n + 1];
    for (int i = 0;i < m;i++) {
        int a, b;
        cin >> a >> b;
        g[b]++; h[a].push_back(b);
    }
    queue<int> q;
    for (int i = 1;i <= n;i++) {
        if (g[i] == 0) q.push(i);
    }
    for (int i = 1;i <= n;i++) {
        int x = q.front();
        q.pop();
        result[i] = x;
        for (int j = 0;j < h[x].size();j++) {
            int y = h[x][j];
            if (--g[y] == 0) q.push(y);
        }
    }
    for (int i = 1;i <= n;i++) {
        cout << result[i] << ' ';
    }
}