#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n;
    cin >> n;
    long long fives = 0;
    for (int i = 5; i < n; i *= 5)
    {
        fives += n / i;
    }
    cout << fives;
}