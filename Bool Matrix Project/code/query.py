'''

Reads in a collection and a Boolean query and prints to STDOUT
the IDs of documents in the collection satisfying the query expression.

The program will be run from the root of the repository.

'''

import sys
import ast
import json
import preprocessing # implements tokenize and normalize text
import precedence # implements the functions to fix precedence
from os.path import exists

'''
Below are the implementation of the basic boolean operators on bit vectors
'''
def term_vector(term):
    if term not in matrix:
        raise Exception("- Error: Term Not Found. -")
    assert term in matrix and len(matrix[term]) == matrix['_M_']
    return matrix[term]

def AND(vector1, vector2):
    assert len(vector1) == matrix['_M_'] and len(vector2) == matrix['_M_']
    result_vector = [0] * matrix['_M_']

    for index in range(matrix['_M_']):
        if vector1[index] == vector2[index] and vector1[index] == 1:
            result_vector[index] = 1

    return result_vector

def OR(vector1, vector2):
    assert len(vector1) == matrix['_M_'] and len(vector2) == matrix['_M_']
    result_vector = [0] * matrix['_M_']

    for index in range(matrix['_M_']):
        if vector1[index] == 1 or vector2[index] == 1:
            result_vector[index] = 1
    
    return result_vector

def NOT(vector):
    assert len(vector) == matrix['_M_']
    result_vector = [0] * matrix['_M_']

    for index in range(matrix['_M_']):
        if vector[index] == 1:
            result_vector[index] = 0
        
        if vector[index] == 0:
            result_vector[index] = 1
    
    return result_vector

'''
Below are the other key functions for the assignment.
'''
extension = ".matrix.json"
def read_matrix(collection):
    '''
    Reads a term-document incidence matrix (inside the 'processed' folder).
    '''
    queries_file = './processed/' + collection + extension

    # checks if it is a valid file.
    if not exists(queries_file):
        print("- Error: File Doesn't Exist. -")
        sys.exit(1)

    # opening the file.
    file = open(queries_file, 'r')
    lines = file.read()

    # Loading the JSON-like data into a Python dictionary
    matrix = ast.literal_eval(lines) 

    file.close()

    return matrix

def document_ids(vector):
    '''
    Returns a list with the IDs of documents corresponding to non-zero entries 
    in the matrix.
    '''
    assert len(vector) == matrix['_M_']
    valid_documents = []

    for index in range(matrix['_M_']):
        if vector[index] == 1:
            valid_documents.append(index + 1)
    
    return valid_documents

def solve_expression(stack):
    '''
    Returns the result of the expression at the top of the stack 
    (as discussed in class)
    '''
    assert type(stack) == list

    answer = stack.pop()
    token = stack.pop()
    while token != "(":
        if (token == ":not:"):
            answer = NOT(answer)
        if (token == ":and:"):  
            operand = stack.pop()
            answer = AND(answer,operand)
        if (token == ":or:"):   
            operand = stack.pop()
            answer = OR(answer,operand)
        token = stack.pop()
    return answer

def answer(tokenized_query):
    '''
    Implements the algorithm for solving expressions discussed in class.
    Must call solveExpression(...) eventually.
    '''
    assert type(tokenized_query) == list
    
    stack = [] # start with empty stack

    for i in range(len(tokenized_query)):
        if 0 <= i:
            token = tokenized_query[i]
            if token in [":not:",":and:",":or:","("]:
                stack.append(token)
            elif token == ")":
                result = solve_expression(stack)
                stack.append(result)
            else:
                v = term_vector(token)
                stack.append(v)


    answer_vector = stack.pop()
    assert len(answer_vector) == matrix['_M_']
    return document_ids(answer_vector)


def tokenize_and_answer(query_expression):
    '''
    Takes a query expression (string), tokenizes it, calls fix_precedence to
    add parenthesis as discussed in class, and calls answer to solve the
    query and return the ids.
    '''
    assert type(query_expression) == str

    fixed_precedence = precedence.fix_precedence(query_expression.split())
    tokenized_query = []

    reserved = set(['(', ')', ':and:', ':or:', ':not:'])

    for token in fixed_precedence:
        if token in reserved:
            tokenized_query.append(token)
        else:
            # note: tokenize/normalize work with lists but we expect a single word here
            terms = preprocessing.normalize(preprocessing.tokenize(token))
            assert len(terms) == 1
            tokenized_query.append(terms[0])

    return answer(['('] + tokenized_query + [')'])


matrix = {}

if __name__ == "__main__":
    '''
    "main()" function goes here
    '''    
    
    # Read the collection name from the command line
    n = len(sys.argv)
    if n != 3:
        print("- Error: Incorrect Number of Arguments -")
        sys.exit(1)

    matrix = read_matrix(sys.argv[1])
    assert type(matrix) == dict  # matrix must be as in the specs

    query = tokenize_and_answer(sys.argv[2])

    # print the IDs of the documents satisfying the query, one per line
    for docID in query:
        print(docID)

    exit(0)