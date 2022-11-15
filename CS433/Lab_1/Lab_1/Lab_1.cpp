// Lab_1.cpp : This file contains the 'main' function. Program execution begins and ends there.


// Quiz 3, q3
/*#include <stdio.h>
void test(void); // Function prototype (description)

int main()
{
    test();
    return 0;
}
void test()
{
    double A = 6, B = 16, C = 0;
    unsigned short cntrl = 0x3FF, stat;
    unsigned char byt;
    __asm
    {
        FINIT; Set FPU to default state
        FLDCW cntrl; Round even, Mask Interrupts

        FLD B; Push SY onto FP stack
        FSQRT; Square root number on stack

        FLD A; Push A onto FP stack
        FMUL ST, ST(0); Multiply A* A result on ST


        FSUB ST, ST(1); SUB top two numbers on stack
        FSTP C; Copy result from stack into HY
    }
    // Binary representation of the 4 bytes, (32 bits)
    printf("Binary:");
    for (int x = 7; x >= 0; x--)
    {
        byt = *((unsigned char*)&C + x);
        for (int y = 128; y > 0; y /= 2)
        {
            if ((y & byt) == 0) printf("0"); else printf("1");
        }
    }
    // Decimal format
    printf("\nDecimal: %3.0lf", C);
    // Hex format
    printf("\nHex:");
    for (int x = 7; x >= 0; x--)
    {
        byt = *((unsigned char*)&C + x);
        printf("%0.2X", (unsigned int)byt);
    }
    // Decimal 4 byte format
    printf("\nDecimal (4bytes):");
    for (int x = 7; x >= 0; x--)
    {
        byt = *((unsigned char*)&C + x);
        printf("%d,", (unsigned int)byt);
    }
}
*/



// Quiz 3, q4
#include <iostream>
#include <stdio.h>
void test(void); // Function prototype (description)
int main()
{
    test();
    return 0;
}
// Put our unmanaged/unsafe asm code in here
void test()
{

    union mmx_word {
        signed __int16 word[4];
        signed __int64 value;
    };

    mmx_word X1 = { 1, 2, 1, 2 }; // 4 Words
    mmx_word Y1 = { 2, 3, 4, 5 };
    mmx_word X2 = { 4, 3, 2, 1 };
    mmx_word Y2 = { 6, 7, 8, 9 };

    mmx_word X = { 0, 0, 0, 0 };
    mmx_word Y = { 0, 0, 0, 0 };

    mmx_word DOT = { 0, 0, 0, 0 };

    __asm
    {

        movq mm0, X1
        movq mm1, X2 // Packed with Unsigned Saturation
        // X1 = X1 * X2
        pmullw mm0, mm1 // 8 words in 2 register -> 8 bytes
       
        // X = X1
        movq X, mm0 // in one register, saturate above 255


        movq mm2, Y1
        movq mm3, Y2
        // Y1 = Y1 * Y2
        pmullw mm2, mm3
        
        // Y = Y1
        movq Y, mm2

        movq mm4, X
        movq mm5, Y
        paddw mm4, mm5

        movq DOT, mm4
    }

    // Bytes
    for (int i = 0; i < 4; i++) printf("%ld, ", (int)(DOT.word[i]));

    // Words as two bytes
    //for (int i = 0; i < 4; i++) printf("%d, %d, ", (unsigned int)(NUM1.word[i]&255),
    //(unsigned int)(NUM1.word[i] /256));

    // Words
    // for (int i = 0; i < 4; i++) printf("%d, ", (unsigned int)(NUM1.word[i]));
    // Floating point value
    //printf("%I64u",(unsigned __int64)NUM1.byte[0]);
}