#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int n, ans = 0, state = 0;
    cin >> n;
    vector<pair<int, int> > meets;
    for (int i = 0;i < n;i++) {
        int begin, end;
        cin >> begin >> end;
        meets.push_back({ begin, 1 });
        meets.push_back({ end, -1 });
    }
    sort(meets.begin(), meets.end());
    for (const auto& meet : meets) {
        state += meet.second;
        ans = max(ans, state);
    }
    cout << ans;
}