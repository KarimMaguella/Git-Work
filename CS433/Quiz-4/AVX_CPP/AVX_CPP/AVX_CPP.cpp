// Build the code using x64 in Release mode
#include <stdint.h>
#include <immintrin.h>
#include <stdio.h>

extern "C"
{
    long  start_tag(void);
    long  end_tag(void);
    long long readTimeStamp(void);;
}

long long startTime, endTime, elapsedTime;
double duration;

int main()
{
    /* Initialize the two argument vectors */
    __m256 total = _mm256_set_ps(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
    __m256 one = _mm256_set_ps(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0);

    //start_tag();
    FILE* fp;
    fopen_s(&fp, "C:\\x64\\AVX_CPP\\x64\\Release\\AVX_Test.csv", "wt");

    for (int j = 0; j < 10; j++)              // Repeat experiment 10 times
    {
        startTime = readTimeStamp();          // Record start time

        /* Add one, ten thousand times*/
        for (int i = 0; i < 10000; i++)       // Run code of interest 10,000 times
        {
            total = _mm256_add_ps(total, one);
            // total = _mm256_add_ps(total, one);
        }

        endTime = readTimeStamp();            // Record stop time
        elapsedTime = endTime - startTime;    // Record cycles usedto run code

        duration = (((double)elapsedTime / 10000.0) / (3.5E9)) * 1e9; // nS

        fprintf(fp, "%d,%lld,%lf\n", j, elapsedTime, duration);     // Write to file 
        //printf("%d,%lld,%lf\n", j, elapsedTime, duration);     // Write to screen
    }

    fclose(fp);

    // end_tag();

     /* Display the elements of the result vector */
    float* f = (float*)&total;
    printf("%f %f %f %f %f %f %f %f\n", f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7]);

    return 0;
}