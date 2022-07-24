#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int n;
    cin >> n;
    vector<int> ip(n);
    for (int i = 0;i < n;i++) {
        cin >> ip[i];
    }
    vector<int> dp(n);
    dp[0] = ip[0];
    int idx = 0;
    for (int i = 0;i < n;i++) {
        if (dp[idx] < ip[i]) {
            dp[++idx] = ip[i];
        }
        else {
            int ii = lower_bound(dp.begin(), dp.end(), ip[i]) - dp.begin();
            dp[ii] = ip[i];
        }
    }
    cout << idx + 1;
}