'''
Compares the output of print_document.py on document #3 of GOOD
'''

import subprocess

print("Testing output of print_document -- expected to PASS")

doc3 = "Testing strategies must include plenty" \
" of debugging." 

program = "./code/print_document.py"
collection = "GOOD"
docID = "3"

output = subprocess.check_output(["python3", program, collection, docID])
answer = output.decode('utf-8').strip()

# compare outputs, word by word
words_answer = answer.split()
words_doc3 = doc3.strip().split()

if len(words_doc3) == len(words_answer):
    for i in range(len(words_answer)):
        if words_doc3[i] != words_answer[i]:
            print("FAIL: The text words don't match.")
            exit(1) # signal error to OS

    # if we reach this point, the answer is correct
    print("PASS")
    exit(0) # signal success to OS

# if we reach this point, the returned document is not as expected
print("FAIL: The number of words in the text doesn't match.")
exit(1) # signal error to OS