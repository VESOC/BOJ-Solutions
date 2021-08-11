#include <bits/stdc++.h>
using namespace std;
#define INF 987654321

typedef long long ll;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    ll nodeCnt, edgeCnt;
    cin >> nodeCnt >> edgeCnt;
    vector<tuple<ll, ll, ll> > edges;
    for (int i = 0;i < edgeCnt; i++) {
        ll from, to, val;
        cin >> from >> to >> val;
        edges.push_back({ from, to, val });
    }
    ll distance[501];
    for (int i = 1; i < nodeCnt + 1; i++) {
        distance[i] = INF;
    }
    distance[1] = 0;
    bool cycle = false;
    for (int i = 1; i <= nodeCnt; i++) {
        for (const auto& edge : edges) {
            ll from, to, val;
            tie(from, to, val) = edge;
            if (distance[from] == INF) continue;
            if (distance[to] <= distance[from] + val) continue;
            distance[to] = distance[from] + val;
            if (i == nodeCnt) cycle = true;
        }
    }
    if (cycle) { cout << -1; return 0; }
    for (int i = 2;i < nodeCnt + 1;i++) {
        if (distance[i] == INF) cout << -1 << '\n';
        else cout << distance[i] << '\n';
    }
}