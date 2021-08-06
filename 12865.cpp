#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int n, k;
    cin >> n >> k;
    int totalValues[101][100001], weights[101], values[101];
    for (int i = 1;i <= n;i++) {
        cin >> weights[i] >> values[i];
    }
    for (int item = 1;item <= n;item++) {
        for (int targetWeight = 1;targetWeight <= k;targetWeight++) {
            if (weights[item] <= targetWeight) {
                totalValues[item][targetWeight] = max(totalValues[item - 1][targetWeight], totalValues[item - 1][targetWeight - weights[item]] + values[item]);
            }
            else {
                totalValues[item][targetWeight] = totalValues[item - 1][targetWeight];
            }
        }
    }
    cout << totalValues[n][k];
}