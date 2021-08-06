#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int n, minIdx;
    cin >> n;
    ll total = 0, minPrice = 1000000000, price;
    vector<ll> roads(n - 1);
    for (int i = 0;i < n - 1;i++) {
        cin >> roads[i];
    }
    for (int i = 0;i < n - 1;i++) {
        cin >> price;
        if (price < minPrice) {
            minPrice = price;
        }
        total += minPrice * roads[i];
    }
    cin >> price;
    cout << total;
}