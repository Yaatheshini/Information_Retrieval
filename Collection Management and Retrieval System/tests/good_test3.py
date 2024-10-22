'''
Compares the output of print_answers on query #4 of GOOD
'''

import subprocess

print("Testing output of print_answers -- expected to PASS")

answer4 = set([5]) 
program = "./code/print_answers.py"
collection = "GOOD"
query = "4"

output = subprocess.check_output(["python3", program, collection, query])
answer = output.decode('utf-8').strip()

# compare outputs, id by id
ids_answer = [int(x) for x in answer.split()]

if len(answer4) == len(ids_answer):
    for i in range(len(ids_answer)):
        if ids_answer[i] not in answer4:
            print("FAIL: The document IDs don't match.")
            exit(1) # signal error to OS

    # if we reach this point, the answer is correct
    print("PASS")
    exit(0) # signal success to OS

# if we reach this point, the returned answer is not as expected
print("FAIL: The number of document IDs don't match.")
exit(1) # signal error to OS
