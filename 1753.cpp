#include <bits/stdc++.h>
using namespace std;
#define INF 987654321

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int v, e, start;
    cin >> v >> e >> start;
    vector<pair<int, int> > adj[v + 1];
    for (int i = 0; i < e;i++) {
        int from, to, val;
        cin >> from >> to >> val;
        adj[from].push_back({ to, val });
    }
    priority_queue<pair<int, int> > pq;
    int distance[v + 1];
    for (int i = 1;i < v + 1;i++) {
        distance[i] = INF;
    }
    distance[start] = 0;
    pq.push({ 0, start });
    while (!pq.empty()) {
        int node = pq.top().second, nodeVal = -pq.top().first; pq.pop();
        for (const auto& edge : adj[node]) {
            int to = edge.first, w = edge.second;
            if (nodeVal + w < distance[to]) {
                distance[to] = nodeVal + w;
                pq.push({ -distance[to], to });
            }
        }
    }
    for (int i = 1;i < v + 1;i++) {
        if (distance[i] == INF) cout << "INF\n";
        else cout << distance[i] << '\n';
    }
}