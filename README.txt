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
to generate potential programs. It uses the output type provided by the user to generate programs according to the grammar defined in the python file
(i have predefined a bunch of operations, including integer arithmetic and a few custom methods). It will evaluate until the memory pool of potential programs reaches
MAX_POOL_SIZE, which is defined by default to be 10,000,000(this corresponds to roughly 1-3 million programs being checked with the default settings)