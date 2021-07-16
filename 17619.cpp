#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

struct P {
    int x1;
    int x2;
    int id;
};

bool cmp(P a, P b) {
    if (a.x1 == b.x1) return a.x2 < b.x2;
    else return a.x1 < b.x1;
}

int main() {
    int N, Q;
    int tmp;
    scanf("%d %d", &N, &Q);
    vector<P> log(N);
    for (int i = 0; i < N; i++) {
        scanf("%d %d %d", &log[i].x1, &log[i].x2, &tmp);
        log[i].id = i+1;
    }
    sort(log.begin(), log.end(), cmp);
    vector<int> group(N+1);
    int groupNum = 0, last = log[0].x2;
    for (int i = 1; i < N; i++) {
        if (log[i].x1 <= last) {
            if (last < log[i].x2) last = log[i].x2;
        } else {
            last = log[i].x2;
            groupNum++;
        }
        group[log[i].id] = groupNum;
    }
    int l1, l2;
    for (int i = 0; i < Q; i++) {
        scanf("%d %d", &l1, &l2);
        printf("%d\n", group[l1]==group[l2]);
    }
}