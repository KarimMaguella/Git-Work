.data
.code
rrand PROC C
rdrand rax
RET
rrand ENDP

rseed PROC C
rdseed rax
RET
rseed ENDP

cpuid_check PROC C
mov eax, 7; Call cpuid eax, 7 and ecx, 0
mov ecx, 0
cpuid
test ebx, 40000h; RDSEED check ebx bit 18
jz L1
mov eax, 'Y'
jmp L2
L1 : mov eax, 'N'
L2 : RET

cpuid_check ENDP
end