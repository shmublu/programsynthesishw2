import ast
import argparse
INT = 1
BOOL = 2
#int functions
_mult = 10
_add = 11
_sub = 12
_div = 13
_sifd = 14


#bool funcs
_isodd = 20
_not = 21

LITERAL_DICT = {INT: {'1','2', '3'}, BOOL: {'True', 'False'}}
FUNCTION_DICT = {}
FUNCTION_DICT[INT] = [_mult, _add, _sub, _div, _sifd]
FUNCTION_DICT[BOOL] = [_isodd, _not]
SPECIAL = {'(', ')', ','}
FUNCTION_TRANSLATION = {}
FUNCTION_TRANSLATION[_mult] = [INT, '*', INT]
FUNCTION_TRANSLATION[_add] = [INT, '+', INT]
FUNCTION_TRANSLATION[_div] = [INT, '/', INT]
FUNCTION_TRANSLATION[_sub] = [INT, '-', INT]
FUNCTION_TRANSLATION[_sifd] = ['squareIfTrueElseDecrement(', INT, ',', BOOL, ')']
FUNCTION_TRANSLATION[_isodd] = ['isOdd(', INT, ')']
FUNCTION_TRANSLATION[_not] = ['not', BOOL]
MAX_POOL_SIZE = 10000000



def synthesize(input_tuples, return_type, examples):
    for tup in input_tuples:
        typ, var_name = tup
        LITERAL_DICT[typ].add(var_name)
    expressions = [[return_type]]
    while(expressions and len(expressions) < MAX_POOL_SIZE):
        current_expression = expressions.pop(0)
        first_nt = find_first_nonterminal(current_expression)
        if first_nt == -1:
            works = run_eval(input_tuples, current_expression, examples)
            if works:
                return works
        else:
            nt_type = current_expression[first_nt]
            #print(current_expression)
            #print(first_nt)
            #print(nt_type)
            translations = []
            if nt_type in LITERAL_DICT:
                translations = LITERAL_DICT[nt_type]
                for lit in translations:
                    new_expr = current_expression[:first_nt] + [lit] + current_expression[(first_nt + 1):]
                    expressions.append(new_expr)
                for nt in FUNCTION_DICT[nt_type]:
                    inserted_expr = FUNCTION_TRANSLATION[nt]
                    new_expr = current_expression[:first_nt] + inserted_expr + current_expression[(first_nt + 1):]
                    expressions.append(new_expr)
    return 'No Solution Found'
                
            #means it is only terminals and we should evaluate it
    
    

def find_first_nonterminal(expr):
    for i in range(len(expr)):
        if isinstance(expr[i], int):
            return i
    return -1
def run_eval(input_tuples, expr, examples):
    eval_expr = ' '.join(expr)
    for pair in examples:
        #inp is a list, out is a value
        inp, out = pair
        test_eval = " "+ eval_expr + " "
        for i, val in enumerate(inp):
            test_eval = test_eval.replace(' ' + input_tuples[i][1] + ' ', ' ' + val + ' ')
        try:
            eval_result = eval(test_eval)
            if eval_result != ast.literal_eval(out):
                return False
        except:
            return False
    return eval_expr
            
def process_input_text_file(fileObject):
    input_tuples = []
    return_type = 0
    examples = []
    line = fileObject.readline()
    splits = line.split(':')
    inputs = splits[0].split(',')
    output = splits[1].strip()
    l = 0
    for i, inp in enumerate(inputs):
        if inp=='INT':
            l=INT
        elif inp=='INT':
            l =BOOL
        input_tuples.append((l, 'x' + str(i)))
    if output=='INT':
        return_type=INT
    elif output=='BOOL':
        return_type=BOOL
    while(True):
        line = fileObject.readline()
        if not line:
            break
        splits = line.split(':')
        inputs = splits[0].split(',')
        output = splits[1].strip()
        example = []
        for i,inp in enumerate(inputs):
            example.append(inp)
        examples.append((example, output))
    return (input_tuples, return_type, examples)
            
            
    
    
    
 
#custom functions
def isOdd(x):
    return x % 2 == 1
def squareIfTrueElseDecrement(x, tf):
    if tf:
        return x * x
    else:
        return x - 1
        
        
      
            
        
        
input_tuples = [(INT, 'x'), (INT, 'y')]
expr = ['x', '*', 'y']
return_type = BOOL
examples = [(['3', '2'], 'False'),(['7', '1'], 'True'), (['3', '1'], 'True'), (['6', '2'], 'True')]
argParser = argparse.ArgumentParser(
                    prog = 'Top Down Synthesizer',
                    description = 'Synthesizes based on a high level specification',
                    epilog = ' ')
argParser.add_argument("-i", "--input", help="input file")
args = argParser.parse_args()
if not args.input:
    print("ERROR: Please specify the input file with -i")
    exit()
try:
    f = open(args.input, "r")
    input_tuples, return_type,  examples = process_input_text_file(f)
    print(synthesize(input_tuples,return_type,examples))
    f.close()
except Exception as e:
    print(e)

