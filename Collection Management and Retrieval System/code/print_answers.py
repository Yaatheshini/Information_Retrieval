'''

Prints the *answers* to a query, as in the collection file, but read from 
a processed file. 
Answers are document IDs and should be printed one per line.

The program will be run from the root of the repository.

'''

import sys
from os.path import exists

# Suggestion: keep the answers in a dictionary, using the query ID as the key
answers = {}
extension = ".PREL" 

def read_answers(collection):
    '''
    Reads a processed collection (inside the 'processed' folder).
    '''
    answers_file = './processed/' + collection + extension

    # checks if it is a valid file.
    if not exists(answers_file):
        print("- Error: Processed Relation File Doesn't Exist. -")
        sys.exit(1)

    # opening the file.
    file = open(answers_file, 'r')
    lines = file.readlines()

    for line in lines:

        # obtaining the first 2 values [1. query id. 2. document id].
        line = line.split(":")
        query_id = int(line[0])

        # creating a key with query id, and an empty list to add values.
        if query_id not in answers.keys():
            answers[int(query_id)] = []
        
        # appending the document id into the list.
        document_ids = line[1].strip('[] \n').split(',')   
        for id in document_ids:
            answers[query_id].append(int(id))

    # closing the file
    file.close()   

def retrieve_answers_to_query(queryID):
    '''
    Returns the answers to a query given its id
    '''

    # TODO: check for errors
    if queryID in answers:
        return answers[queryID]
    else:
        print("Error. Query does not exit in Answers.")
        sys.exit(1)

if __name__ == "__main__":
    '''
    main() function
    '''
    # TODO: read the collection name from command line
    if len(sys.argv) != 3:
        print("Incorrect Number of Command Line Arguements.")
        sys.exit(1)

    # TODO: read query ID from command line
    collection_name = sys.argv[1]
    query_id = int(sys.argv[2])

    # TODO: check for invalid parameters
    read_answers(collection_name)

    # Check if the query ID exists in the collection
    if query_id not in answers.keys():
        print(f"Error: Query '{query_id}' not found in collection '{collection_name}'.")
        sys.exit(1)
        

    # TODO: print the query answers to STDOUT
    output = retrieve_answers_to_query(query_id)     
    for number in output:
        print(number)

    exit(0)
