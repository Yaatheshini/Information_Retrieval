'''

Prints the *contents* of a query, as in the collection file, but read from 
a processed file.

The program will be run from the root of the repository.

'''

import sys
from os.path import exists

# Suggestion: keep the quries in a dictionary, using the ID as the key
queries = {}
extension = ".PQRY"

def read_queries(collection):
    '''
    Reads a processed collection (inside the 'processed' folder).
    '''
    queries_file = './processed/' + collection + extension

    # checks if it is a valid file.
    if not exists(queries_file):
        print("- Error: File Doesn't Exist. -")
        sys.exit(1)
    
    # opening .PQRY and reading into the new dictionary 
    file = open(queries_file, 'r')
    lines = file.readlines()
    text = ''
    key = 0
    for line in lines:
        if line.strip().isnumeric() == False:
            text += line
        else:
            if key not in queries.keys() and text != '':
                queries[int(key)] = text
                text = ''
            key = line.strip() 

    # adding last case.
    if key != 0 and text != '':
        queries[int(key)] = text

    # closing the file
    file.close()     

def retrieve_query(queryID):
    '''
    Returns a query given its id
    '''

    # TODO: check for errors
    if queryID in queries:
        return queries[queryID]
    else:
        print("Error. Query does not exit in Collection.")
        sys.exit(1)

if __name__ == "__main__":
    '''
    main() function
    '''
    # TODO: read the collection name from command line
    if len(sys.argv) != 3:
        print("Incorrect Number of Command Line Arguements.")
        exit(0)

    # TODO: read query ID from command line
    collection_name = sys.argv[1]
    query_id = int(sys.argv[2])

    # TODO: check for invalid parameters
    read_queries(collection_name)
    
    # Check if the query ID exists in the collection
    if query_id not in queries.keys():
        print(f"Error: Query '{query_id}' not found in collection '{collection_name}'.")
        exit(1)

    # TODO: print the query to STDOUT
    print(retrieve_query(query_id))

    exit(0)