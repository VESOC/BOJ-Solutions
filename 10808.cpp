#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s;
    int ans[26] = {
        0,
    };
    cin >> s;
    for (const char &c : s)
    {
        ans[c - 'a']++;
    }
    for (const int &v : ans)
    {
        printf("%d ", v);
    }
}