#include <bits/stdc++.h>
using namespace std;

bool cmp(pair<int, int> a, pair<int, int> b) {
    if (a.second == b.second)
        return a.first < b.first;
    else
        return a.second < b.second;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n, d, ans = 0;
    cin >> n;
    vector<pair<int, int> > routes;
    for (int i = 0;i < n;i++) {
        int a, b;
        cin >> a >> b;
        routes.push_back({ min(a, b), max(a, b) });
    }
    cin >> d;
    sort(routes.begin(), routes.end(), cmp);
    priority_queue<int, vector<int>, greater<int>> begins;
    for (const auto& route : routes) {
        if (route.second - route.first > d) continue;
        begins.push(route.first);
        while (!begins.empty()) {
            if (begins.top() < route.second - d) begins.pop();
            else {
                ans = max(ans, (int)begins.size());
                break;
            }
        }
    }
    cout << ans;
}