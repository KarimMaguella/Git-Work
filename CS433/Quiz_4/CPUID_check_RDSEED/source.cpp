// Random generator - Broadwell and higher, i5=5xxx or higher
#include <stdio.h>

using namespace std;

extern "C"
{
    long long rrand(void);
    long long rseed(void);
    long long cpuid_check(void);
}

int main(int argc, char* argv[])
{
    long long x;

    for (int i = 0; i <= 4; i++)
    {
        if (cpuid_check() == 'Y')
        {
            x = rseed();
            printf("RDSEED: %d\n", x);
        }
        else
        {
            x = rrand();
            printf("RDRAND: %d\n", x);
        }
    }

    return 0;
}