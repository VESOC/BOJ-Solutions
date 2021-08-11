#include <bits/stdc++.h>
using namespace std;
#define INF 987654321

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int n, e;
    cin >> n >> e;
    int dist[101][101];
    for (int i = 1;i <= n;i++) {
        for (int j = 1;j <= n;j++) {
            dist[i][j] = INF;
        }
    }
    for (int i = 0;i < e;i++) {
        int from, to, val;
        cin >> from >> to >> val;
        dist[from][to] = min(dist[from][to], val);
    }
    for (int k = 1;k <= n;k++) {
        for (int i = 1;i <= n;i++) {
            for (int j = 1;j <= n;j++) {
                if (dist[i][k] != INF && dist[k][j] != INF)
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
    for (int i = 1;i <= n;i++) {
        for (int j = 1;j <= n;j++) {
            if (i == j || dist[i][j] == INF)
                cout << 0 << " ";
            else
                cout << dist[i][j] << " ";
        }
        cout << '\n';
    }
}