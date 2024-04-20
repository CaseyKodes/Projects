#       CSE 3666 Lab 4
#	TAG: 5fd71ac11b8a14746aa31ed0caf142197fb20839

	.data
	.align	2	
word_array:     .word
        0,   10,   20,  30,  40,  50,  60,  70,  80,  90, 
        100, 110, 120, 130, 140, 150, 160, 170, 180, 190,
        200, 210, 220, 230, 240, 250, 260, 270, 280, 290,
        300, 310, 320, 330, 340, 350, 360, 370, 380, 390,
        400, 410, 420, 430, 440, 450, 460, 470, 480, 490,
        500, 510, 520, 530, 540, 550, 560, 570, 580, 590,
        600, 610, 620, 630, 640, 650, 660, 670, 680, 690,
        700, 710, 720, 730, 740, 750, 760, 770, 780, 790,
        800, 810, 820, 830, 840, 850, 860, 870, 880, 890,
        900, 910, 920, 930, 940, 950, 960, 970, 980, 990

        # code
        .text
        .globl  main
main:   
	addi	s0, x0, -1
	addi	s4, x0, -1
	addi	s5, x0, -1
	addi	s6, x0, -1
	addi	s7, x0, -1

	# help to check if any saved registers are changed during the function call
	# could add more...

        # la      s1, word_array
        lui     s1, 0x10010      # starting addr of word_array in standard memory config
        addi    s2, x0, 100      # 100 elements in the array

        # read an integer from the console
        addi    a7, x0, 5
        ecall

        addi    s3, a0, 0       # keep a copy of v in s3
        
        # call binary search
        addi	a0, s1, 0
        addi	a1, s2, 0
        addi	a2, s3, 0
        jal	ra, binary_search

exit:   addi    a7, x0, 10      
        ecall

#### Do not change lines above

#code to translate
#int     binary_search(int a[], int n, int v)
#  { int     rv;
#    if (n == 0) {        // nothing in the array
#       rv = -1;
#       goto  f_exit; }   // return -1
#    int half = n / 2;   // integer division
#    int half_v = a[half];
#    if (half_v == v) {
#        rv = half;}
#    else if (v < half_v) {
#        // search the first half, excluding a[half]
#       rv = binary_search(a, half, v); }
#    else {v > half_v
#       // search the second half, excluding a[half]
#        int left = half + 1;
#        // &a[left] means the address of a[left]
#        rv = binary_search(&a[left], n - left, v);
#        if (rv >= 0) {
#            rv += left;}}
#f_exit: return rv;}

binary_search:
#TODO
        addi sp, sp, -12 # allocating space in the stack 
        sw s1, 0(sp)
        sw s2, 4(sp)
        sw ra, 8(sp)
        bne a1, x0, endif # if the list has elements go to endif
        addi a0, x0, -1 # if not make a0 -1
        beq x0, x0, f_exit # go to return section
        
endif:
	srai s1, a1, 1 # s1 is a1/2
	slli t0, s1, 2 # t0 is now s1*4 
	add t0, a0, t0 # t0 is now a1*8 + a0
	lw a6, 0(t0) # loading the address of t0 into a6
	bne a6, a2, elseif # if a6 != a2 got to elseif
	addi a0, s1, 0 # a0 is s1
	beq x0, x0, f_exit # go to return section
	
elseif:
	blt a6, a2, else # if a6<a2 go to else
	addi a1, s1, 0 # a1 is s1
	jal ra, binary_search # recall binary search 
	beq x0, x0, f_exit # go to return section

else:
	addi s2, s1, 1 # s2 is now s1+1
	slli t1, s2, 2 # t1 s2 *4
	add a0, a0, t1 # a0 is now a0+t1
	sub a1, a1, s2 # a1 now a1-s2
	jal ra, binary_search # recall binary search 
	blt a0, x0, f_exit # got to return section
	add a0, a0, s2 # a0 is a0+s2

f_exit:
	# loading values from stack 
        lw s1, 0(sp)
        lw s2, 4(sp)
        lw ra, 8(sp)
        # moving stack pointer 
        addi sp, sp, 12
        # returning
        jalr x0, ra, 0
