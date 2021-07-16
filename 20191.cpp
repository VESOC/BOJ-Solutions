#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solution()
{
    string S, T;
    cin >> S;
    cin >> T;
    vector<vector<int> > next(26);
    for (int i = 0; i < T.length(); i++)
    {
        next[T[i] - 'a'].push_back(i);
    }

    int chkCnt = 0, chkIdx;
    for (int i = 0; i < 26; i++)
    {
        if (!next[i].empty())
        {
            chkCnt++;
            chkIdx = i;
        }
    }
    if (chkCnt == 1 && T[chkIdx] == S[0])
        return (S.length() + T.length() - 1) / T.length();

    int cnt = 1, pos = -1, before_pos = -1;
    for (const char& c : S)
    {
        int k = c - 'a';
        if (next[k].empty())
            return -1;

        int left = 0, right = next[k].size();
        while (left < right)
        {
            int mid = (left + right) / 2;
            if (before_pos < next[k][mid])
                right = mid;
            else
                left = mid + 1;
        }
        pos = left;
        if (pos == next[k].size())
        {
            cnt++;
            pos = 0;
        }
        before_pos = next[k][pos];
    }

    return cnt;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout << solution();
}