#include <bits/stdc++.h>
using namespace std;

#define MAX 10001
typedef pair<int, int> pii;
int connected[MAX], result[MAX], visited[MAX];
vector<pii> fStart[MAX], fEnd[MAX];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int n, m;
    cin >> n >> m;
    for (int i = 0;i < m;i++) {
        int from, to, val;
        cin >> from >> to >> val;
        fStart[from].push_back({ to, val });
        fEnd[to].push_back({ from, val });
        connected[to]++;
    }
    int start, end;
    cin >> start >> end;
    queue<int> q;
    q.push(start);
    while (!q.empty()) {
        int x = q.front();
        q.pop();
        for (int i = 0;i < fStart[x].size();i++) {
            int node = fStart[x][i].first, time = fStart[x][i].second;
            result[node] = max(result[node], time + result[x]);
            if (--connected[node] == 0) q.push(node);
        }
    }
    int count = 0;
    q.push(end);
    while (!q.empty()) {
        int x = q.front();
        q.pop();
        for (int i = 0;i < fEnd[x].size();i++) {
            int node = fEnd[x][i].first, time = fEnd[x][i].second;
            if (result[x] == result[node] + time) {
                count++;
                if (visited[node] == 0) {
                    q.push(node);
                    visited[node] = 1;
                }
            }
        }
    }
    cout << result[end] << '\n' << count;
}