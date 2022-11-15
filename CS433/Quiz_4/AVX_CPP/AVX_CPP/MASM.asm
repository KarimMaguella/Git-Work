.data
.code
start_tag PROC C; START tag is 0x111
mov ebx, 111h; Put the bytes BB 11 01 00 00 64 67 90
db 64h, 67h, 90h; mov ebx, 111h followed by xchg eax, eax
RET
start_tag ENDP

end_tag PROC C; En tag is 0x2222
mov ebx, 222h
db 64h, 67h, 90h
RET
end_tag ENDP
end