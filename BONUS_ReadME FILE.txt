For these Four instructions we are using the Type B Binary encoding- Register and Immediate Type

In these instaructions we apply the operation on the value stored in a register and then store the resultant value back in the same register.

OPCODE:Function

"10011":addi,
"10100":subi,
"10101":muli,
"10110":divi,
"10111":pow


addi-> Adds an immediate value into regi then stores the answer in regi.
subi-> Sutracts the imediate value from the value stored in regi and then stores the answer back inside regi.
muli-> Multiplies the value in regi with the immediate and then stores the resultant in regi.
divi-> Divies the value in regi with immediate and then stores the resultant in regi. We have applied a check for the immediate to not be 0.
pow-> Raises the value stored in regi to the power of the immediate value given and then stores it back to the same regi.

Checks->
We have applied checks if the immediate value is greater than 7 bits, immediate in divi is not equal to 0. 

NOTE-regi=Some arbitary register except PC and FLAG.