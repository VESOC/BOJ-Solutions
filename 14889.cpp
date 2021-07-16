#include <bits/stdc++.h>

using namespace std;

int n, diff = 1 << 30;
int member[20][20];
bool visited[20];

void makeTeam(int cnt, int cur) {
    if (cnt == n / 2) {
        int tA = 0, tB = 0;
        for (int i = 0; i < n;i++) {
            for (int j = i + 1;j < n;j++) {
                if (visited[i] && visited[j]) {
                    tA += member[i][j] + member[j][i];
                }
                else if (!visited[i] && !visited[j]) {
                    tB += member[i][j] + member[j][i];
                }
            }
        }
        diff = min(diff, abs(tA - tB));
    }
    else {
        for (int i = cur;i < n;i++) {
            if (!visited[i]) {
                visited[i] = true;
                makeTeam(cnt + 1, i + 1);
                visited[i] = false;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(); cout.tie();

    cin >> n;

    for (int i = 0;i < n;i++) {
        for (int j = 0;j < n;j++) {
            cin >> member[i][j];
        }
    }
    makeTeam(0, 0);
    cout << diff;
}