# transalte the follwing into RISC-V
# for (i = 0; i < 100; i += 1)
# B[i] = A[i] + 4;

        .data                   #data segment
        .align 2

src:   .word   
  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,
 10,  11,  12,  13,  14,  15,  16,  17,  18,  19,
 20,  21,  22,  23,  24,  25,  26,  27,  28,  29,
 30,  31,  32,  33,  34,  35,  36,  37,  38,  39,
 40,  41,  42,  43,  44,  45,  46,  47,  48,  49,
 50,  51,  52,  53,  54,  55,  56,  57,  58,  59,
 60,  61,  62,  63,  64,  65,  66,  67,  68,  69,
 70,  71,  72,  73,  74,  75,  76,  77,  78,  79,
 80,  81,  82,  83,  84,  85,  86,  87,  88,  89,
 90,  91,  92,  93,  94,  95,  96,  97,  98,  99,
100, 101, 102, 103, 104, 105, 106, 107, 108, 109,
110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
120, 121, 122, 123, 124, 125, 126, 127

dst:    .space  1024

        .text
        .globl  main

main: 
add s1, x0, x0 # counter for loop
lui s2, 0x10010 # starting address of A
addi s3, s2, 512 # starting address of B
addi t1, x0, 100 # limit of loop

# key: s1=i, s2=A address, s3=B address, t2=offset, t3=base+offset
# key: t4=where we store loaded value 
loop:
	# calculation
	slli t2, s1, 2 # t2=i*4
	
	add t3, s2, t2 # adding offset to A address
	lw t4, 0(t3) # t4 loaded value from A
	
	addi t4, t4, 4 # t4+=4
	
	add t3, s3, t2 # adding offset to B address
	sw t4, 0(t3) # t4 stored in B
	
	#looping
	addi s1, s1, 1 # incirment i
	blt s1, t1, loop
exit: