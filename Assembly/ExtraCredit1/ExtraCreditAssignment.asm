; Gabriel Snider
; 3/31/2022

.586
.MODEL FLAT
.STACK  4096

.DATA
nbrArray    DWORD    25, 47, 15, 50, 32, 95 DUP (?)
nbrElts     DWORD    5
aveminfive  DWORD    0
aveplufive  DWORD    0
.CODE
main        PROC
; find sum and average
            mov    eax,0            ; sum := 0
            lea    ebx,nbrArray     ; get address of nbrArray
            mov    ecx,nbrElts      ; count := nbrElts
            jecxz  quit             ; quit if no numbers
forCount1:  add    eax,[ebx]        ; add number to sum
            add    ebx,4            ; get address of next array elt
            loop   forCount1        ; repeat nbrElts times

            cdq                     ; extend sum to quadword
            idiv   nbrElts          ; calculate average

; add 10 to each array element below average
            lea    ebx,nbrArray     ; get address of nbrArray
            mov    ecx,nbrElts      ; count := nbrElts

forCount2:  cmp    [ebx],eax        ; number < average ?
            jnl    endIfSmall       ; continue if not less
            add    DWORD PTR [ebx], 10   ; add 10 to number
            mov    aveminfive,eax   ; copies average to aveminfive
            mov    aveplufive,eax   ; copies average to aveplufive
            sub    aveminfive, 5    ; subtracts five from aveminfive
            add    aveplufive, 5    ; adds five to aveplufive
            mov    edx, aveminfive  ; copies aveminfive to edx
            cmp    [ebx], edx       ; compares ebx to edx
            jge    aveCheck1        ; jumps if ebx is greater than or equal than edx
            jmp    endIfSmall       ; jmp endIfSmall

aveCheck1:
           mov edx, 0               ; copies 0 to edx
           mov edx, aveplufive      ; copies aveplufive to edx
           cmp DWORD PTR[ebx], edx  ; compares ebx to edx
           jl  setEqual             ; jumps to setEqual if ebx is less than edx
           jmp endIfSmall           ; makes sure that ebx gets set back to what it needs to be.

setEqual:
          mov [ebx], eax            ; sets ebx to the average stored in eax

endIfSmall:
            add    ebx,4            ; get address of next array elt
            loop   forCount2        ; repeat
            
quit:       mov   eax, 0      ; exit with return code 0
            ret
main        ENDP
END
