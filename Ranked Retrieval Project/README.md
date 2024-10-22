# Compilation/execution instructions

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

# Sources consulted

List all websites/sources consulted.

https://www.geeksforgeeks.org/python-lemmatization-with-nltk/
https://www.w3schools.com/python/ref_random_choice.asp
