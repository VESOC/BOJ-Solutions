#include <bits/stdc++.h>
using namespace std;

string p, s;

vector<int> makeTable() {
    int subSize = s.size();
    vector<int> table(subSize);
    int j = 0;
    for (int i = 1;i < subSize;i++) {
        while (j > 0 && s[i] != s[j]) {
            j = table[j - 1];
        }
        if (s[i] == s[j]) {
            table[i] = ++j;
        }
    }
    return table;
}

void KMP() {
    vector<int> table = makeTable();
    int pSize = p.size(), sSize = s.size();
    int j = 0;
    for (int i = 0;i < pSize;i++) {
        while (j > 0 && p[i] != s[j]) {
            j = table[j - 1];
        }
        if (p[i] == s[j]) {
            if (j == sSize - 1) {
                cout << 1;
                return;
            }
            else {
                j++;
            }
        }
    }
    cout << 0;
}

int main() {
    cin >> p >> s;
    KMP();
}