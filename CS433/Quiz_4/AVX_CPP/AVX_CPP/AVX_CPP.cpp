// Build the code using x64 in Release mode
// Run this code using the Intel Software Emulator using the following command line
// sde -snb -d -omix my_mix.out -iform 1 -global_region -start_ssc_mark 111:repeat -stop_ssc_mark 222:repeat -- C:\Users\Alien\source\repos\AVX_CPP\x64\Release\AVX_CPP.exe
#include <stdint.h>
#include <immintrin.h>
#include <stdio.h>

extern "C"
{
    long  start_tag(void);
    long  end_tag(void);
}

int main()
{
    /* Initialize the two argument vectors */
    __m256 total = _mm256_set_ps(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
    __m256 one = _mm256_set_ps(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0);

    /* Add one, one thousand times*/
    //start_tag();
    for (int i = 0; i < 1000; i++)
    {
        total = _mm256_add_ps(total, one);
    }
    //end_tag();

    /* Display the elements of the result vector */
    float* f = (float*)&total;
    printf("%f %f %f %f %f %f %f %f\n", f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7]);

    return 0;
}