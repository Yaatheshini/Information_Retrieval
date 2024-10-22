'''

Reads all documents in the collection file into memory and writes
term-document incidence matrix to the processed folder.

The program will be run from the root of the repository.

'''

import sys
import json
import preprocessing # implements tokenize and normalize text
from os.path import exists

extension = ".ALL"

def read_documents(collection):
    '''
    Reads the documents in the collection (inside the 'collections' folder).
    '''

    assert type(collection) == str
    corpus_file = './collections/' + collection + extension

    # checks if it is a valid file.
    if not exists(corpus_file):
        print("- Error: File Doesn't Exist. -")
        sys.exit(1)

    # opening the file.
    file = open(corpus_file, 'r')
    lines = file.readlines()
    key = 0
    documents = {}

    for index in range(len(lines)):

        # checking if it is index.
        if lines[index][0:2] == '.I':
            key = int(lines[index].split()[1])

            # checking if the key already exists within the documents dictionary.
            if key in documents.keys():
                print("- Error: Key Already In Documents -")
                sys.exit(1)

            # setting the documents key: value pair.
            documents[key] = ''

        # checking if it is text (abstract).
        if lines[index][0:2] == '.W':
            temp = index + 1

            # adding text to the string until we encounter one of the five possible states.
            while temp < len(lines) and lines[temp][0:2] not in ['.I', '.T', '.A', '.W', '.X']:
                documents[key] += lines[temp]
                temp += 1

    print(f'{len(documents)} documents read in total')
    return documents

def build_incidence_matrix(documents):
    '''
    Build term-document incidence matrix.
    Documents are given as mappings id -> text.
    '''

    assert type(documents) == dict

    matrix = {}  # Initialize an empty matrix
    tokenized = {}

    # Tokenize and normalize text for each document
    for docID in documents:
        original_text = documents[docID]
        tokenized[docID] = preprocessing.normalize(preprocessing.tokenize(original_text))

    # Initialize an empty list for each term
    for docID in documents:
        for token in tokenized[docID]:
            if token not in matrix:
                matrix[str(token)] = [0] * len(documents)  # Initialize with zeros

    # Update the incidence matrix
    for docID in documents:
        for token in tokenized[docID]:
            matrix[token][docID - 1] = 1  # Mark the presence of the term in the document

    # Add the total number of documents (_M_) as the first element
    sorted_matrix = {'_M_': len(documents)}

    # Populate the rest of the sorted matrix
    for key in sorted(matrix):
        if key != '_M_':
            sorted_matrix[key] = matrix[key]

    return sorted_matrix

def write_matrix(collection, matrix):
    '''
    Writes the data structure to the processed folder
    '''

    assert type(matrix) == dict
    matrix_file = './processed/' + collection + '.matrix.json'

    # checks if it is a valid file.
    if exists(matrix_file):
        print("- Error: Processed File Already Exists. -")
        sys.exit(1)

    # dumping matrix dictionary into json file.
    file = open(matrix_file, 'w')

    file.write("{\n")
    for key, value in matrix.items():
        file.write('    "' + key + '": ' + json.dumps(value) + ",\n")
        
    file.write("}")

    file.close()
    
if __name__ == "__main__":
    # Read the collection name from the command line
    n = len(sys.argv)
    if n != 2:
        print("- Error: Incorrect Number of Arguments -")
        sys.exit(1)

    documents = read_documents(sys.argv[1])
    matrix = build_incidence_matrix(documents)
    write_matrix(sys.argv[1], matrix)

    # Print 'SUCCESS' to STDOUT if all went well
    print("SUCCESS")
    exit(0)