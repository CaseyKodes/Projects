# translate the follwoing into RISC-V
# for (i = 0; i < 16; i += 1) {
# for (j = 0; j < 8; j += 1)
# { T[i][j] = 256 * i + j;} }

main:
addi t1, x0, -1 # this will be the counter for the outer loop 
		# start at -1 so we can incriment every time we enter outloop
addi t3, x0, 16 # this is the limit for the outer loop
add t2, x0, x0  # this will be the counter for the inner loop
addi t4, x0, 8  # this is the limit for the inner loop 

lui s9 0x10000 # just so s9 has some value

# key t1=i, t2=j, t3=16, t4=8, t5=temp sum, t6=offset, s1=32*j, s2=4i, s3 = 32j+4i
outloop:
	add t2, x0, x0 # resetting the value of t2 to 0
	addi t1, t1, 1 # incriment value of t1
	blt t1, t3, inloop # if i<16 do the calculation
	beq x0, x0, exit # else exit program
inloop:
	# actual calculation start here
	slli t5, t1, 8 # 256*i is the same as slli i, i, 8
	add t5, t5, t2 # t5 is now 256 * i + j
	
	# now we neeed to figure out where to store t5 in memory 
	# if we think about the 2D array as being smushed into a 1D array then we just 
	# need to adjust offset but the length of a word for every itteration
	slli s1, t1, 5 # s1 = 32*i
	slli s2, t2, 2 # s2 = 4*j
	add s3, s1, s2 # s3 =31j+4i
	# s9 holds the address of T increase by 4 bytes or a single word every time we store a value
	# when we get to a new array in the 2d array j increases which adds 32 to the offset
	# this is why because i was just 8 but it went back to 0 but we need to keep moving up in memory
	add t6, s3, s9
	sw t5 0(t6) 
	
	# looping mechanics 
	addi t2, t2, 1 # incriment j
	beq t2, t4, outloop # if j=8 go to outer loop
	beq x0, x0, inloop # else go to inner loop
exit: