#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int n;
    cin >> n;
    long long ways[1000001], modulVal = 1000000009;
    ways[1] = 1;
    ways[2] = 2;
    ways[3] = 4;
    for (int j = 4;j <= 1000000;j++) {
        ways[j] = (ways[j - 1] + ways[j - 2] + ways[j - 3]) % modulVal;
    }
    while (n--) {
        int test;
        cin >> test;
        cout << ways[test] << '\n';
    }
}