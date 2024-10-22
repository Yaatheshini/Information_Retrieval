'''
Compares the output of print_query on query #5 of GOOD
'''

import subprocess

print("Testing output of print_query -- expected to PASS")

query5 = "Goodbyes and Goodnights greeting message pictures." \

program = "./code/print_query.py"
collection = "GOOD"
query = "5"

output = subprocess.check_output(["python3", program, collection, query])
answer = output.decode('utf-8').strip()

# compare outputs, word by word
words_answer = answer.split()
words_query5 = query5.strip().split()

if len(words_query5) == len(words_answer):
    for i in range(len(words_answer)):
        if words_query5[i] != words_answer[i]:
            print("FAIL: The text words don't match.")
            exit(1) # signal error to OS

    # if we reach this point, the answer is correct
    print("PASS")
    exit(0) # signal success to OS

# if we reach this point, the returned answer is not as expected
print("FAIL: The number of words in the text doesn't match.")
exit(1) # signal error to OS