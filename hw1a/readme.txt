My algorithm impliments the toy DES algorithm exactly as specified.
The program takes in 3 command line arguments for the decrypt or 
encrypt commands.
The first one is the infile which is hex input.
The second one is the outfile which is the file the program will 
output to (also hex)
The third one is the key in binary to be used

The first thing my program does is generate the two keys to be used.
First it permutes the key according the specification then it splits 
it into 2 and left shifts them. After that it reduced the key back
to 8 bits according to the specification. It repeates this process 
to form the 2nd key after left shifting the key one more time.

After creating the keys it breaks the data into 8 bit blocks and
sends them to be turned into cyphertext. First it modifies the 
plaintext bits with an initial permutation. Then it splits the bits 
into two halfs, left and right. 

The right gets sent to the f function to be expanded to 8 bits
according to the permutation rules. Then it get xor with the 8 bit
key. Then it gets split to l and r which use the substition table
to make a substition and reduce it to two bits. Then these bits
are combined and permuted again.

Now the result of the f function gets xor with the left from above.
This cycle now repeates again with the 2nd key and the previous right
becoming the next left and the result of the xor becoming the next
right.

After this you do the inverse initial permutation and you get the
cipher text.