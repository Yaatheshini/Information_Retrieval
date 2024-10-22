'''

Prints the *contents* of a document, as in the corpus, but read from 
a processed file.

The program will be run from the root of the repository.

'''

import sys
from os.path import exists

# Suggestion: keep the documents in a dictionary, using the ID as the key
documents = {}
extension = ".PALL"

def read_documents(collection):
    '''
    Reads a processed collection (inside the 'processed' folder).
    '''
    corpus_file = './processed/' + collection + extension

    # checks if it is a valid file.
    if not exists(corpus_file):
        print("- Error: File Doesn't Exist. -")
        sys.exit(1)
    
    # opening .PALL and reading into the new dictionary 
    file = open(corpus_file, 'r')
    lines = file.readlines()
    text = ''
    key = 0
    for line in lines:
        if line.strip().isnumeric() == False:
            text += line
        else:
            if key not in documents.keys() and text != '':
                documents[int(key)] = text
                text = ''
            key = line.strip() 
    
    # adding last case.
    if key != 0 and text != '':
        documents[int(key)] = text

    # closing the file
    file.close()     

def retrieve_document(docID):
    '''
    Returns a document given its id
    '''

    # TODO: check for errors
    if docID in documents:
        return documents[docID]
    else:
        print("Error. Document does not exit in Collection.")
        sys.exit(1)

if __name__ == "__main__":
    '''
    main() function
    '''
    # TODO: read the collection name from command line
    if len(sys.argv) != 3:
        print("Incorrect Number of Command Line Arguements.")
        exit(0)

    # TODO: read document ID from command line
    collection_name = sys.argv[1]
    document_id = int(sys.argv[2])

    # TODO: check for invalid parameters

    read_documents(collection_name)

    # Check if the document ID exists in the collection
    if document_id not in documents.keys():
        print(f"Error: Document '{document_id}' not found in collection '{collection_name}'.")
        exit(1)

    # TODO: print the document to STDOUT
    print(retrieve_document(document_id))

    exit(0)