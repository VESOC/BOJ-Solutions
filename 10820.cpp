#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s;
    while (getline(cin, s))
    {
        if (!s.size())
            break;
        int upper = 0, lower = 0, space = 0, number = 0;
        for (const char &c : s)
        {
            if (isupper(c))
            {
                upper++;
            }
            else if (islower(c))
            {
                lower++;
            }
            else if (isdigit(c))
            {
                number++;
            }
            else
            {
                space++;
            }
        }
        printf("%d %d %d %d\n", lower, upper, number, space);
    }
}