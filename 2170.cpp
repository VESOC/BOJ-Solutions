#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie();cout.tie();
    int n;
    cin >> n;
    vector<pair<int, int> > lines(n);
    for (int i = 0;i < n;i++) {
        cin >> lines[i].first >> lines[i].second;
    }
    sort(lines.begin(), lines.end());
    pair<int, int> range = lines[0];
    int diff = 0;
    for (int i = 1;i < n;i++) {
        if (range.first <= lines[i].first && lines[i].first <= range.second) {
            range.second = max(range.second, lines[i].second);
        }
        else {
            diff += range.second - range.first;
            range = lines[i];
        }
    }
    diff += range.second - range.first;
    cout << diff;
}