#include <iostream>
#include <string>
using namespace std;

int main()
{
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    string A = to_string(a) + to_string(b);
    string B = to_string(c) + to_string(d);
    cout << stoll(A) + stoll(B);
}