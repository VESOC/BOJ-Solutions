#include <iostream>
#define MIN(a, b) (((a) < (b)) ? (a) : (b))
using namespace std;

long long getNumOfTargets(long long v, int target)
{
    long long ans = 0;
    for (long long i = target; i <= v; i *= target)
    {
        ans += v / i;
    }
    return ans;
}

int main()
{
    long long n, m, fives, twos;
    scanf("%lld %lld", &n, &m);
    fives = getNumOfTargets(n, 5) - getNumOfTargets(m, 5) - getNumOfTargets(n - m, 5);
    twos = getNumOfTargets(n, 2) - getNumOfTargets(m, 2) - getNumOfTargets(n - m, 2);
    printf("%lld", MIN(fives, twos));
}
