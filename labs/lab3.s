# CSE 3666
        
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
        lui     s1, 0x10010     # hard-coded src address
        addi    s3, s1, 512     # s3 is the destination array

        # read n, the number of words to shuffle
        # n is even and 2 <= n <= 128
        addi    a7, x0, 5
        ecall
        # n is in a0

        # TODO:
        # write a loop to shuffle n words
        # the address of the source array src is in s1
        # the address of the destination array dst is in s3
        # register s2 will store the address of the second half of src
        # the folloiwng code can use any t and a registers 
        
	addi t0, x0, 0		# counter
	add s2, a0, a0		# s2 is no 2n
	add s2, s2, s1		# s2 is now 2n+1 meaning first value of right half
	srai a0, a0, 1		# a0 is no2 n/2 loop only runs n/2 times
	
loop:	beq t0, a0, exit	
	#key - t0 = i, t1 = offset, t2 = loading index, t3 = word/data/int to store, storing index

	slli t1, t0, 2		# i * 4	= offset	
	
	# t2 is the address of the element on the left side 
	add t2, t1, s1		# base (left hand side aka s1) + offset
	# t3 is the value of the element on the left side 
	lw t3, 0(t2)		# load from address calc'd above
	
	add t4, t1, s3		# base (right side dst aka s3) + i (offset -> i * 4)
	add t4, t4, t1		# base + i + i
	#storing element from left side in final destination 
	sw t3, 	0(t4)		# store in dst
	
	# t2 is the address of the element on the right side 
	add t2, t1, s2		# base (Right hand side aka s2) + offset
	# t3 is the value of the element on the right side 
	lw t3, 0(t2)		# load from address calc'd above
	
	addi t4, t4, 4		# base (dst aka s3) + offset (indexing into i + i + 1)
	# storing element from right side in the final destination  
	sw t3, 0(t4)		# store in dst
		
	addi t0, t0, 1		# i++
	beq x0, x0, loop	# restart loop


exit:   addi    a7, x0, 10      # syscall to exit
        ecall   
