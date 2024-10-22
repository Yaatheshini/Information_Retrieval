# TODOs

1. **SUBMIT** the URL of this repository on eClass **well before the deadline**.
2. Write compilation/execution instructions for the TA below.
3. List the names and CCID(s) of the student(s) submitting the assignment.
4. List all sources consulted while completing the assignment.

# Compilation/execution instructions

**NOTE**: TAs and instructors **do not** have superuser privileges on the CS lab machines. Provide instructions that a regular user can follow to run your programs. **Make sure to test your instructions.**

```
Reading the .ALL collection:
1: python3 ./code/build_index.py CISI_simplified

Finding the top 10 relevant documents to a query [NOTE: collection, queries, scoring scheme, method, and number of retrieved documents can be altered]:
2. python3 ./code/query.py CISI_simplified ltn l 10 "What is information science?  Give definitions where possible."

Evaluating query.py through the various metrics [NOTE: scoring scheme, method, number of random queries, number of retrieved documents and metrics can be altered]:
3. python3 ./code/evaluation.py CISI_simplified ltn l 10 10 mrr

Testing all possible scoring schemes, methods, number of random queries [10, 80], number of retrieved documents [10, 860, 1710] and metrics, a number of times:
4. python3 ./code/testfile.py 
```

# Students

|Student name| CCID |
|------------|------|
|Yaatheshini Ashok   |yaathesh      |
|Vishal Sivakumar   |vsivakum      |

# Sources consulted

List all websites/sources consulted.
https://www.geeksforgeeks.org/python-lemmatization-with-nltk/
https://www.w3schools.com/python/ref_random_choice.asp
