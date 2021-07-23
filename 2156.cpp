#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int n, data[10001], sum[10001];
    cin >> n;
    for (int i = 1;i <= n;i++) {
        cin >> data[i];
    }
    sum[1] = data[1];
    sum[2] = sum[1] + data[2];
    for (int i = 3;i <= n;i++) {
        sum[i] = max(sum[i - 2] + data[i], sum[i - 3] + data[i - 1] + data[i]);
        sum[i] = max(sum[i], sum[i - 1]);
    }
    cout << sum[n];
}