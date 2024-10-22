'''
Checks whether the processed document file gets created, and it shouldn't.
'''

import sys
import subprocess

print("-" * 150)
print("'Testing output of read_corpus -- expected to FAIL")
print("before reaching print_documents as read_corpus does")
print("the error handling.")
print("-" * 150)

program = "./code/read_corpus.py"
collection = "BAD"

try:
    subprocess.check_output(["python3", program, collection])
    print("PASS")

except subprocess.CalledProcessError as temp:
    temp_command = ' '.join(temp.cmd)
    temp_output = temp.output.strip().decode('utf-8')
    raise RuntimeError("\n\n" + "-" * 150 + "\nCommand '{}' returns Error (code {}) meaning FAIL: {}\n".format(temp_command, temp.returncode, temp_output) + "-" * 150).with_traceback(None) from None