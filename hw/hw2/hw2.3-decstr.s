# Addition of decimal strings
# strings are stored in global data section 
        .data   
dst:    .space  128
str1:   .space  128
str2:   .space  128
# instructions are in text section
        .text
main: 
        # load adresses of strings into s1, s2, and s3
        # s3 is dst, where we store the result 
        lui     s3, 0x10010 
        addi    s1, s3, 128
        addi    s2, s1, 128
        # read the first number as a string
        addi    a0, s1, 0
        addi    a1, x0, 100
        addi    a7, x0, 8
        ecall
        # read the second number as a string
        addi    a0, s2, 0
        addi    a1, x0, 100
        addi    a7, x0, 8
        ecall
        # useful constants
        addi    a4, x0, '0'
        addi    a5, x0, 10
        
########################################################################################
        #TODO
        # write a loop to find out the number of decimal digits in str1
        # the loop searches for the first character that is less than '0' 
        add s4, x0, x0
strlen:
	slli t2, s4, 0 # t2 is s4*1
	add t2, t2, s1
	lb t1, 0(t2)
	addi s4, s4, 1 # increasing count of str1 len
	# if t1 is less than 0 it is not a numeric character so we should stop doing calculations
	blt t1, a4, leave
	beq x0, x0, strlen
leave:  
	# remove 2 from s4 makes the reandom characters at the end of the final desination disapear
	addi s4, s4, -2
	
	# printing length of input strings
	# this includes the \n at the end of each string
	addi    a0, s4, 0
        addi    a7, x0, 1
        #ecall
        
# key: len of strings=s4, t1=str1 element, t2=offset, t3=str2 element, t6=9(limit of addition)
	addi t6, x0, 9 # limit of addition before carry is needed
	addi t4, x0, 0 # carry variable will be used when t1+t1>9
calc:
	# Note that we assume str1, str2, and dst have the same number of 
        # decimal digits. 
        slli t2, s4, 0 # shift for offset 1 byte
        add t2, t2, s1 # str1 address
        lb t1, 0(t2) # str1 element loaded 
        slli t2, s4, 0
        add t2, t2, s2 # srt2 address
        lb t3, 0(t2) # str2 element loaded
        sub t1, t1, a4 # numerical value of t1 now converted
        sub t3, t3, a4 # numerical value of t3 now converted 
        add t5, t1, t3, # t1 and t3 added 
        add t5, t5, t4 # t5 now including carry variable
        addi t4, x0, 0 # reset carry variable to 0
        
        bgt t5, t6, carry # if the sum of the two elements if more than 9 we need to keep track of a carry
	beq x0, x0, skip # skip carry part if sum is not greater than 9  	
	
carry:
	# this spot will be used to lower t5 and keep track of a carry 
	sub t5, t5, a5 # lowers t5 by 10 
	addi t4, x0, 1 # make carry variable 1
	
        # We then write a loop to add str1 and str2, and save the result in 
        # dst also known as s3. 
skip:   	
        add t5, t5, a4 # changing t5 back into a char
        slli t2, s4, 0 # shifting offset
        add t2, t2, s3 # final address stored in t2/offset
        sb t5, 0(t2) # storing the now char value back into s3
        addi s4, s4, -1 # decramenting s4 by 1
        bge s4, x0, calc
        
        # Remember that dst should have a terminating NULL.
        # this is taken care of automatically since after we find the length
        # of the input strings we remove 2
        # find length of output
	add s4, x0, x0
outputlen:
	slli t2, s4, 0 # t2 is s4*1
	add t2, t2, s3
	lb t1, 0(t2)
	addi s4, s4, 1 # increasing count of str1 len
	# if t1 is less than 0 it is not a numeric character so we should stop doing calculations
	blt t1, a4, leavefin
	beq x0, x0, outputlen
leavefin:
	#print the length of the output
	addi s4, s4, -1 # this removes the counting of the null character
	addi    a0, s4, 0
        addi    a7, x0, 1
        #ecall
        
########################################################################################

        # end of the loop
        # print the result
print:
        addi    a0, s3, 0
        addi    a7, x0, 4
        ecall
exit:
        addi    a7, x0, 10
        ecall
