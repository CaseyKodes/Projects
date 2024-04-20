#       CSE 3666 uint2decstr
        .globl  main
        .text
main:   
        # create an array of 128 bytes on the stack
        addi    sp, sp, -128
        # copy array's address to a0
        addi    a0, sp, 0
	# set all bytes in the buffer to 'A'
        addi    a1, x0, 0       # a1 is the index
	addi	a2, x0, 128
	addi	t2, x0, 'A'
clear:
        add     t0, a0, a1
	sb	t2, 0(t0)
        addi    a1, a1, 1
	bne	a1, a2, clear
        # change -1 to other numbers to test
        # you can use li load other numbers for testing
        # li      a1, 36663666
        addi	a1, zero, -1
	jal	ra, uint2decstr
        # print the string
        addi    a0, sp, 0
        addi    a7, x0, 4
        ecall

exit:   addi    a7, x0, 10      
        ecall

# char * uint2decstr(char *s, unsigned int v) 
# the function converts an unsigned 32-bit value to a decimal string
# Here are some examples:
# 0:    "0"
# 2022: "2022"
# -1:   "4294967295"
# -3666:   "4294963630"
uint2decstr:
# key; s0=10, s1=r, s2=s[0] 
	# setting s0 to 10 since the number 10 is used multiple times
	addi s0, x0, 10
	# we do the storing outside of the if call just incase 
	# the if block is not executed
	# putting return address into memory since the second 
	# function call changes it 
	addi sp, sp, -4
	sw ra, 0(sp)
	# we should not be changing v forever when we divide by 10
	# only changing it in the call, when we get past the call
	# we should be using the original v
	addi sp, sp, -4
	sw a1, 0(sp)
	# if statement seeing is v>=10
	bge a1, s0, recall
	beq x0, x0, skip
	recall:
		# recall uint2decstr with s and v/10
		divu a1, a1, s0
		jal ra, uint2decstr
	skip:
	# getting v back from the stack 
	lw a1, 0(sp)
	addi sp, sp, 4
	# modulo v and 10 = r
	remu s1, a1, s0
	# s[0] = r + '0'
	addi s2, s1, '0'
	# storing statements to put the values back in the proper 
	# spot of the char array 
	sw s2, 0(a0)
	sw x0, 4(a0)
	# loading return address back from stack 
	lw ra, 0(sp)
	addi sp, sp, 4
	# a0 is return value we need to 
	# set it to the address of a[1]
	add a0, x0, a1
	jalr ra, x0, 0