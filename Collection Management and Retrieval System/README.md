# TODOs

1. **SUBMIT** the URL of this repository on eClass **well before the deadline**.
2. Write compilation/execution instructions for the TA below.
3. List the CCID(s) of student(s) working on the project.
4. List all sources consulted while completing the assignment.

# Compilation/execution instructions

**NOTE**: TAs and instructors **do not** have superuser privileges on the CS lab machines. Provide instructions that a regular user can follow to run your programs. **Make sure to test your instructions.**

```
PYTHON PROGRAMS:

=> code for processing collections
1: Name of python program: read_corpus.py
   Purpose of the test: Reads all documents in the collection file into memory and writes the data structure to the processed folder.
   Sample output of the program: SUCCESS or Appropriate Error Messages

2: Name of python program: read_queries.py
   Purpose of the test: Reads all queries in the collection file into memory and writes the data structure to the processed folder.
   Sample output of the program: SUCCESS or Appropriate Error Messages

3: Name of python program: read_answers.py
   Purpose of the test: Reads answers to queries in the collection file into memory and writes the data structure to the processed folder.
   Sample output of the program: SUCCESS or Appropriate Error Messages

```
```
=> output of your programs in 'code'
4: Name of python program: print_document.py
   Purpose of the test: Prints the *contents* of a document, as in the corpus, but read from a processed file.
   Input ID: 3
   Sample output of the program:
      The relationships between the organization and control of writings
      and the organization and control of knowledge and information will
      inevitably enter our story, for writings contain, along with much else, a
      great deal of mankind's stock of knowledge and information.  Bibliographical
      control is a form of power, and if knowledge itself is a form of power,
      as the familiar slogan claims, bibliographical control is in a certain sense
      power over power, power to obtain the knowledge recorded in written
      form.  As writings are not simply, and not in any simple way, storehouses of
      knowledge, we cannot satisfactorily discuss bibliographical control as
      simply control over the knowledge and information contained in writings.

5: Name of python program: print_query.py
   Purpose of the test: Prints the *contents* of a query, as in the collection file, but read from a processed file.
   Input ID: 3
   Sample output of the program:
      What is information science?  Give definitions where possible.

6: Name of python program: print_answers.py
   Purpose of the test: Prints the *answers* to a query, as in the collection file, but read from a processed file. 
   Input ID: 6
   Sample output of the program:
      400

```
```
=> programs to test our code (default provided test cases)
7: Name of python program: test1.py
   Purpose of the test: Compares the output of print_document.py on document #30 of CISI
   Sample output of the program:
      Testing output of print_document -- expected to PASS
      PASS

8: Name of python program: test2.py
   Purpose of the test: Compares the output of print_query on query #34 of CISI
   Sample output of the program:
      Testing output of print_query -- expected to PASS
      PASS

9: Name of python program: test3.py
   Purpose of the test: Compares the output of print_answers on query #82 of CISI
   Sample output of the program:
      Testing output of print_answers -- expected to PASS
      PASS

```
```
=> programs to test our code (Good and Bad Collections built by us)
POINT TO NOTE:
  The good collections test each of the print_XYZ.py specific outputs and ensures that the expected and actual outputs match.
  The bad collections, since they're not (and cannot be) processed, tests the read_XYZ.py programs and returns an error message as to why it fails. It will show a runtime error, but the details between the boxes are the actual outputs of the program. 

10: Name of python program: good_test1.py
    Purpose of the test: Compares the output of print_document.py on document #3 of GOOD
    Testing Document ID: 3
    Sample output of the program:
      Testing output of print_document -- expected to PASS
      PASS

11: Name of python program: good_test2.py
    Purpose of the test: Compares the output of print_query on query #5 of GOOD
    Testing Query ID: 5
    Sample output of the program:
      Testing output of print_query -- expected to PASS
      PASS

12: Name of python program: good_test3.py
    Purpose of the test: Compares the output of print_answers on query #4 of GOOD
    Testing Query ID: 4
    Sample output of the program:
      Testing output of print_answers -- expected to PASS
      PASS

13: Name of python program: bad_test1.py
    Purpose of the test: Checks whether the processed document file gets created, and it shouldn't.
    Sample output of the program:
      ------------------------------------------------------------------------------------------------------------------------------------------------------
      'Testing output of read_corpus -- expected to FAIL
      before reaching print_documents as read_corpus does
      the error handling.
      ------------------------------------------------------------------------------------------------------------------------------------------------------
      Traceback (most recent call last):
        File "/Users/vishalsivakumar/Desktop/2ND YEAR/WINTER TERM 2024/CMPUT 361/ASSIGNMENTS/1. COLLECTION AND IR/./tests/bad_test1.py", line 24, in <module>
          raise RuntimeError("\n\n" + "-" * 150 + "\nCommand '{}' returns Error (code {}) meaning FAIL: {}\n".format(temp_command, temp.returncode, temp_output) + "-" * 150).with_traceback(None) from None
      RuntimeError: 
      
      ------------------------------------------------------------------------------------------------------------------------------------------------------
      Command 'python3 ./code/read_corpus.py BAD' returns Error (code 1) meaning FAIL: - Error: Key Already In Documents -
      ------------------------------------------------------------------------------------------------------------------------------------------------------

14: Name of python program: bad_test2.py
    Purpose of the test: Checks whether the processed queries file gets created, and it shouldn't.
    Sample output of the program:
      ------------------------------------------------------------------------------------------------------------------------------------------------------
      'Testing output of read_queries -- expected to FAIL
      before reaching print_query as read_queries does
      the error handling.
      ------------------------------------------------------------------------------------------------------------------------------------------------------
      Traceback (most recent call last):
        File "/Users/vishalsivakumar/Desktop/2ND YEAR/WINTER TERM 2024/CMPUT 361/ASSIGNMENTS/1. COLLECTION AND IR/./tests/bad_test2.py", line 24, in <module>
          raise RuntimeError("\n\n" + "-" * 150 + "\nCommand '{}' returns Error (code {}) meaning FAIL: {}\n".format(temp_command, temp.returncode, temp_output) + "-" * 150).with_traceback(None) from None
      RuntimeError: 
      
      ------------------------------------------------------------------------------------------------------------------------------------------------------
      Command 'python3 ./code/read_queries.py BAD' returns Error (code 1) meaning FAIL: - Error: Value Doesn't Exist For ID = 2 -
      ------------------------------------------------------------------------------------------------------------------------------------------------------

15: Name of python program: bad_test3.py
    Purpose of the test: Checks whether the processed answers file gets created, and it shouldn't.
    Sample output of the program:
      ------------------------------------------------------------------------------------------------------------------------------------------------------
      'Testing output of read_answers -- expected to FAIL
      before reaching print_answers as read_answers does
      the error handling.
      ------------------------------------------------------------------------------------------------------------------------------------------------------
      Traceback (most recent call last):
        File "/Users/vishalsivakumar/Desktop/2ND YEAR/WINTER TERM 2024/CMPUT 361/ASSIGNMENTS/1. COLLECTION AND IR/./tests/bad_test3.py", line 24, in <module>
          raise RuntimeError("\n\n" + "-" * 150 + "\nCommand '{}' returns Error (code {}) meaning FAIL: {}\n".format(temp_command, temp.returncode, temp_output) + "-" * 150).with_traceback(None) from None
      RuntimeError: 
      
      ------------------------------------------------------------------------------------------------------------------------------------------------------
      Command 'python3 ./code/read_answers.py BAD' returns Error (code 1) meaning FAIL: - Error: Document Inputted Not Valid -
      ------------------------------------------------------------------------------------------------------------------------------------------------------

```
```
=> programs to test our code (Generalized Bonus Cases from CISI files [1-20])
POINT TO NOTE:
   These bonus files have taken the first 20 cases presented in the provided CISI files, and generalized the testing process, taking random values each time.

16: Name of python program: bonus_1.py
    Purpose of the test: Generalizes the output of print_document.py from documents 1-20 of CISI
    Sample output of the program:
      Testing output of print_document -- expected to PASS
      Document generated is:  13
      PASS

17: Name of python program: bonus_2.py
    Purpose of the test: Generalizes the output of print_query.py from documents 1-20 of CISI
    Sample output of the program:
      Testing output of print_query -- expected to PASS
      Query generated is:  16
      PASS

18: Name of python program: bonus_3.py
    Purpose of the test: Generalizes the output of print_answers.py from documents 1-20 of CISI
    Sample output of the program:
      Testing output of print_answers -- expected to PASS
      Answer generated is:  5
      PASS
```

```
COMMAND LINES:

=> code for processing collections
1: python3 ./code/read_corpus.py CISI
2: python3 ./code/read_corpus.py GOOD
3: python3 ./code/read_corpus.py BAD
4: python3 ./code/read_queries.py CISI
5: python3 ./code/read_queries.py GOOD
6: python3 ./code/read_queries.py BAD
7: python3 ./code/read_answers.py CISI
8: python3 ./code/read_answers.py GOOD
9: python3 ./code/read_answers.py BAD

=> output of your programs in 'code'
10: python3 ./code/print_document.py CISI document_id
11: python3 ./code/print_query.py CISI query_id
12: python3 ./code/print_answers.py CISI query_id

=> programs to test our code (default provided test cases)
13: python3 ./tests/test1.py
14: python3 ./tests/test2.py
15: python3 ./tests/test3.py

=> programs to test our code (Good and Bad Collections built by us)
16: python3 ./tests/good_test1.py
17: python3 ./tests/bad_test1.py
18: python3 ./tests/good_test2.py
19: python3 ./tests/bad_test2.py
20: python3 ./tests/good_test3.py
21: python3 ./tests/bad_test3.py

=> programs to test our code (Generalized Bonus Cases from CISI files [1-20])
22: python3 ./tests/bonus_1.py
23: python3 ./tests/bonus_2.py
24: python3 ./tests/bonus_3.py
```

# Students

|       Student name       |   CCID   |
|--------------------------|----------|
|Yaatheshini Ashok Kumar   | yaathesh |
|Vishal Sivakumar          | vsivakum |

List all websites/sources consulted:

https://www.simplilearn.com/tutorials/python-tutorial/python-check-if-file-exists
https://stackoverflow.com/questions/27920837/subprocess-check-output-returned-non-zero-exit-status-1
https://stackoverflow.com/questions/63004235/how-to-remove-the-traceback-most-recent-call-last-in-python-when-raising-an-ex
