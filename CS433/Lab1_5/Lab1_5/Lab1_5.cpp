// Lab1_5.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <stdio.h>   
#include <xmmintrin.h>  // SIMD intrinsics
#include<iostream>

using namespace std;

extern "C"
{
	void sse_add(float* inputArray, float* outputArray);
}


int main(int argc, char* argv[])
{
	// Arrays containing multiples of 4 floats (4x32=128bits,16 bytes) xmm0, xmm1
	float inputArray[8] = { 1.0,  2.0,  3.0,  4.0,	0.0, -1.0, -3.0, 20.0 };
	float outputArray[4] = {};


	sse_add(inputArray, outputArray);   // Test function

	for (int i = 0; i < 4; i++) printf("%f,", outputArray[i]);

	printf("\nFinished\n");

	return 0;
}