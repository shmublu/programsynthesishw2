To run:
Put your type at the top of a text file(only supported types are BOOL and INT). Operands are separated by commas, and the output is separated by a colon.
I.e: 
INT,BOOL:BOOL

The next lines should contain your actual examples, separated in the same way. I.e:
4,True:True
4,False:False
5,True:False
7,False:True


The tool is run with:
python hw2v2.py -i <example file>
or
python3 hw2v2.py -i <example file>



EDITS FROM HW1:
HW1 was a brute force solver that supported integer arithmetic. This is a toop-down solver that uses types as a kind of context-free grammar
to generate potential programs. It uses the typing to eliminate programs that do not match