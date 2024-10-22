'''

Reads answers to queries in the collection file into memory and writes
the data structure to the processed folder.

The program will be run from the root of the repository.

'''

import sys
from os.path import exists

# Suggestion: keep the answers in a dictionary, using the query ID as the key
answers = {}
valid_documents_id = []
valid_queries_id = []
extension = ".REL" 
temp_extension1 = ".ALL"
temp_extension2 = ".QRY"
processed_extension = ".PREL"

def read_documents(collection):
    '''
    Reads the documents in the collection (inside the 'collections' folder).
    '''
    corpus_file = './collections/' + collection + temp_extension1

    # checks if it is a valid file.
    if not exists(corpus_file):
        print("- Error: Documents File Doesn't Exist. -")
        sys.exit(1)
    
    # opening the file.
    file = open(corpus_file, 'r')
    lines = file.readlines()

    for index in range(len(lines)):

        # checking if it is index.
        if lines[index][0:2] == '.I':
            key = int(lines[index].split()[1])

            # checking if the key already exists within the documents dictionary.
            if key in valid_documents_id:
                continue

            valid_documents_id.append(key)

    # closing the file
    file.close()    

def read_queries(collection):
    '''
    Reads the queries in the collection (inside the 'collections' folder).
    '''
    queries_file = './collections/' + collection + temp_extension2

    # checks if it is a valid file.
    if not exists(queries_file):
        print("- Error: Queries File Doesn't Exist. -")
        sys.exit(1)

    # opening the file.
    file = open(queries_file, 'r')
    lines = file.readlines()
    key = 0

    for index in range(len(lines)):

        # checking if it is index.
        if lines[index][0:2] == '.I':
            key = int(lines[index].split()[1])

            # checking if the key already exists within the queries dictionary.
            if key in valid_queries_id:
                continue
            
            valid_queries_id.append(key)
        
    # closing the file
    file.close()       

def read_answers(collection):
    '''
    Reads the answers in the collection (inside the 'collections' folder).
    '''
    answers_file = './collections/' + collection + extension

    # checks if it is a valid file.
    if not exists(answers_file):
        print("- Error: Relation File Doesn't Exist. -")
        sys.exit(1)

    # filling the lists of valid id's for documents and queries.
    read_documents(collection)
    read_queries(collection)

    # opening the file.
    file = open(answers_file, 'r')
    lines = file.readlines()

    for line in lines:

        # obtaining the first 2 values [1. query id. 2. document id].
        temp = line.split()
        query_id = int(temp[0])
        document_id = int(temp[1])

        # checking if query id is valid.
        if query_id not in valid_queries_id:
            print("- Error: Query Inputted Not Valid -")
            sys.exit(1)
        
        # checking if document id is valid.
        if document_id not in valid_documents_id:
            print("- Error: Document Inputted Not Valid -")
            sys.exit(1)

        # creating a key with query id, and an empty list to add values.
        if query_id not in answers.keys():
            answers[query_id] = []
        
        # appending the document id into the list.
        answers[query_id].append(document_id)

def write_answers(collection):
    '''
    Writes the data structure to the processed folder
    '''
    processed_file = './processed/' + collection + processed_extension

    # checks if it is a valid file.
    if exists(processed_file):
        print("- Error: Processed File Already Exists. -")
        sys.exit(1)

    file = open(processed_file, 'w')

    for key in answers.keys():
        print(key, ":", answers[key], file=file)

    file.close()

if __name__ == "__main__":
    '''
    main() function
    '''

    # TODO: read the collection name from command line
    n = len(sys.argv)

    # Checking if correct number of command line arguements are provided
    if n != 2:
        print("- Error: Incorrect Number of Arguments -")
        sys.exit(1)

    read_answers(sys.argv[1])
    write_answers(sys.argv[1])
    
    # print 'SUCCESS' to STDOUT if all went well
    print("SUCCESS")

    exit(0)