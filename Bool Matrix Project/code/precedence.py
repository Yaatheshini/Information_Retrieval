'''

Implements the functions to "fix" the precendence of operators in the 
query expression provided by the user by "wrapping" higher precedence
subexpressions in parenthesis, making sure that:

1. parenthesis provided by the user are left untouched.
2. :not: operators are "fixed" first.
3. :and: expressions are "fixed" next.

'''

def find_par_exp_forward(expression):
    '''
    Finds the index of the token within expression correspondin to the end of 
    the parenthetical expression in front of a :not: or an :and: operator.
    '''
    assert type(expression) == list
    depth = 0
    index = 0
    for i in range(len(expression)):
        if expression[i] == "(":
            depth += 1
        elif expression[i] == ")":
            depth -= 1
        if expression[i] == ')' and depth == 0:
            return i 
    return len(expression) - 1


def find_par_exp_backward(expression):
    '''
    Finds the index of the token within expression correspondin to the start of 
    the parenthetical expression behind an :and: operator.
    '''
    assert type(expression) == list
    depth = 0
    index = len(expression) - 1
    for i in range(len(expression)-1,-1,-1):
        token = expression[i]
        if token == ")":
            depth += 1
            
        elif token == "(":
            depth -= 1 
        
        if expression[i] == '(' and depth == 0:
            return i
            
        elif expression[i] in [':and:',':or:'] and i != len(expression) - 1:
            return i + 1
    return 0
    
def fix_precedence_AND(expression, start=0):
    '''
    Finds and "wraps" all exp1 :and: exp2 in the query expression as discussed in class.
    '''
    assert type(expression) == list

    index = start
    while index < len(expression):
        token = expression[index]
        if token == ":and:":
            # Look for the start of expr1 and the end of expr2
            expr1_start = find_par_exp_backward(expression[:index])
            expr2_end = find_par_exp_forward(expression[index + 1:])
            expr2_end += index + 1  # Adjust index for expr2

            # Wrap expr1 :and: expr2 in parentheses if necessary
            if expression[expr1_start] != "(":
                expression.insert(expr1_start, "(")
                expression.insert(expr2_end + 2, ")")

            # Update index to continue searching for :and: operators
            index += 3  # Adjust index for the inserted parentheses
        else:
            index += 1

    return expression

def fix_precedence_NOT(expression):
    """
    Finds and "wraps" all :not: expressions in the query expression.
    """
    assert type(expression) == list

    index = 0
    while index < len(expression):
        if expression[index] == ":not:":

            expression.insert(index, '(')
            expr2_end = find_par_exp_forward(expression[index + 1:])
            expression.insert(expr2_end + index + 2, ")")            
        
        index += 2
            
    return expression


def fix_precedence(expression):
    '''
    Fixes the precedence of an entire expression
    '''
    
    assert type(expression) == list
    step1 = fix_precedence_NOT(expression)
    step2 = fix_precedence_AND(step1)
    
    return step2