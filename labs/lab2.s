#       CSE 3666 Lab 2

        .globl  main

        .text
main:   
        # use system call 5 to read integer
        addi    a7, x0, 5
        ecall
        addi    s1, a0, 0       # copy to s1

        # TODO
        # Add you code here
        #   reverse bits in s1 and save the results in s2
        addi s4, x0, 32
        add t0, s1, x0
        add s2, x0, x0
loop:
	bge s3, s4, loopexit
	slli s2, s2, 1
	andi t1, t0, 1
	or s2, s2, t1
	srli t0, t0, 1
	addi s3, s3, 1
	beq x0, x0, loop
	
loopexit:
        #   print s1 in binary, with a system call
        addi a7, x0, 35
	add a0, s1, x0
	ecall
	
        #   print newline
        addi a0, x0, 10
	addi a7, x0, 11
	ecall 
	
        #   print '=' if s1 is palindrome, otherwise print s2 in binary
        beq s1, s2, pal
        
        # printing flipped 
        addi a7, x0, 35
	add a0, s2, x0
	ecall
	
	# to skip printing the = 
        beq x0, x0, skip
pal: 
	addi a0, x0, 61
	addi a7, x0, 11
	ecall 
	
skip:
        #   print newline
        addi a0, x0, 10
	addi a7, x0, 11
	ecall 
	
        # exit
exit:   addi    a7, x0, 10      
        ecall