#include <bits/stdc++.h>
using namespace std;


bool visited[1000001];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    int f, s, g, u, d;
    cin >> f >> s >> g >> u >> d;


    queue<pair<int, int>> q;
    q.emplace(s, 0);
    visited[s] = true;
    while (!q.empty()) {
        auto [floor, cnt] = q.front();
        q.pop();
        if (floor == g) {
            cout << cnt << '\n';
            exit(0);
        }
        if (floor + u <= f && !visited[floor + u]) {
            visited[floor + u] = true;
            q.emplace(floor + u, cnt + 1);
        }
        if (floor - d > 0 && !visited[floor - d]) {
            visited[floor - d] = true;
            q.emplace(floor - d, cnt + 1);
        }
    }
    cout << "use the stairs";
}