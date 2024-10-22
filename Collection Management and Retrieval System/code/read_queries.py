'''

Reads all queries in the collection file into memory and writes
the data structure to the processed folder.

The program will be run from the root of the repository.

'''

import sys
from os.path import exists

# Suggestion: keep the queries in a dictionary, using the ID as the key
queries = {}
extension = ".QRY"
processed_extension = ".PQRY"

def read_queries(collection):
    '''
    Reads the queries in the collection (inside the 'collections' folder).
    '''
    queries_file = './collections/' + collection + extension

    # checks if it is a valid file.
    if not exists(queries_file):
        print("- Error: File Doesn't Exist. -")
        sys.exit(1)

    # opening the file.
    file = open(queries_file, 'r')
    lines = file.readlines()
    key = 0

    for index in range(len(lines)):

        # checking if it is index.
        if lines[index][0:2] == '.I':
            prev_key = key
            key = int(lines[index].split()[1])

            # checking if the key already exists within the queries dictionary.
            if key in queries.keys():
                print("- Error: Key Already In Queries -")
                sys.exit(1)
            

            # setting the queries key: value pair.
            queries[key] = ''

        # checking if it is text (abstract).
        if lines[index][0:2] == '.W':
            temp = index + 1

            # adding text to the string until we encounter one of the five possible states.
            while temp < len(lines) and lines[temp][0:2] not in ['.I', '.T', '.A', '.W', '.B']:
                queries[key] += lines[temp]
                temp += 1

    # checking for missing values.
    for key in queries.keys():
        if queries[key] == '':
            print("- Error: Value Doesn't Exist For ID = " + str(key) + " - ")
            sys.exit(1)

    # closing the file
    file.close()       


def write_queries(collection):
    '''
    Writes the data structure to the processed folder
    '''
    processed_file = './processed/' + collection + processed_extension

    # checks if it is a valid file.
    if exists(processed_file):
        print("- Error: Processed File Already Exists. -")
        sys.exit(1)

    file = open(processed_file, 'w')

    for key in queries.keys():
        print(key, file=file)
        print(queries[key].strip(), file=file)

    file.close()
    
if __name__ == "__main__":
    '''
    main() function
    '''
    
    # read the collection name from command line
    n = len(sys.argv)


    # Checking if correct number of command line arguements are provided
    if n != 2:
        print("- Error: Incorrect Number of Arguments -")
        sys.exit(1)
    
    read_queries(sys.argv[1])
    write_queries(sys.argv[1])

    # print 'SUCCESS' to STDOUT if all went well
    print("SUCCESS")

    exit(0)