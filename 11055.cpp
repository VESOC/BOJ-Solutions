#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int n;
    cin >> n;
    int data[1000], sum[1000];
    for (int i = 0;i < n;i++) {
        cin >> data[i];
        sum[i] = data[i];
    }
    int M = 0;
    for (int i = 0;i < n;i++) {
        for (int j = 0;j < i;j++) {
            if (data[j] < data[i]) {
                sum[i] = max(sum[i], sum[j] + data[i]);
            }
        }
        M = max(M, sum[i]);
    }
    cout << M;
}