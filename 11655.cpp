#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s;
    getline(cin, s);
    for (const char &c : s)
    {
        if (isupper(c))
        {
            printf("%c", (c - 'A' + 13) % 26 + 'A');
        }
        else if (islower(c))
        {
            printf("%c", (c - 'a' + 13) % 26 + 'a');
        }
        else
        {
            printf("%c", c);
        }
    }
}