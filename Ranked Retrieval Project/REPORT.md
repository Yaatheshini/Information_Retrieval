# Introduction: 
In this assignment, we have various scoring parameters based on the tf-idf scheme and whether we normalize it or not. Further expanding upon the possibilities:

**1. tf**: This is the term frequency within the document. The various scoring methods include:
‘n’: Natural tf, where it is just the raw term frequency within the document.
‘l’ : Logarithmic tf where we compute weight -> (  if tf > 0   -> 1 + log(tf)
                                                   else        -> 0


**2. idf**: This is inversely proportional to informativeness, where the terms with high DF are function/common content words. The various scoring methods include:
‘n’: Natural idf where the value is 1.
‘t’: Logarithmic idf where the weight is the total number of documents (M), and DF is the number of documents the term is present -> log (M/DF)


With the tf-idf values, we can compute a score = tf * idf (based on any tf-idf scheme).

**3. Normalization**: Due to the advantages provided to longer documents by regular dot-product scoring, we normalize it via:
‘n’: No normalization.
‘c’: Cosine Normalization where we score by cosine similarity.

Based on each set of scoring methods, we can have 8 possible permutations of scoring functions, such as  'ltn', 'lnn', 'nnn', 'ntn', 'ltc', 'lnc', 'nnc', 'ntc'.

# Metrics
The program evaluation.py allows the use of two different evaluation metrics:

**1. Mean Average Precision (MAP)**: Metric where the mean average precision is computed, where MAP is the sum of the average precisions of each query (which are the sum of the precisions of relevant and retrieved documents, overall divided by the number of relevant documents retrieved), which is the overall divided by the number of queries.

**2. Mean Reciprocal Rank (MRR)**: Metric where it finds the rank of the first relevant document. This is computed by the sum of the reciprocal ranks for each query, which is divided by the number of queries processed overall.

# Methodology
We have built a testfile.py, which tests for every possible parameter we could use for the command line with a given set of values (Restricted to CISI_simplified collections). Explained below, in the order of the ‘for’ loops within the test file:

**1. K**: This is the number of documents to be retrieved by query.py. We are giving 3 possible values, the lowest, middle, and all documents retrieved, to compare how the number of documents retrieved affects the MAP and MRR with all scoring schemes. The values it can be are 10, 860, 1710.

**2. R**: This is the number of queries to be selected by evaluation.py. We are giving 2 possible values (with duplicates) to compare how the number of queries used affects the MAP and MRR with all scoring schemes. The values it can be are 10 or 80.

**3. Scoring Schemes**: This is a list of all possible permutations of scoring schemes that the user can input. It’s used to check which scheme retrieves the most relevant documents for various documents retrieved and queries ranked. The values it can be are 'ltn', 'lnn', 'nnn', 'ntn', 'ltc', 'lnc', 'nnc', 'ntc'

**4. Method**: These are the various ways of tokenizing and normalizing our terms in the document and query in order to query based on a lemmatized or stemmed inverted index (built by build_index.py prior). It’s used to check which method retrieves more relevant documents. The values it can be are ‘l’ or ‘s’.

**5. Metric**: Finally, we have our list of metrics, which is our way of evaluating the retrieved documents of query.py to check how relevant the retrieved documents are. 
Overall, we run this program using the command:
```python3 ./code/testfile.py```

# Results
| K | R | Scoring Scheme  | Method | Metric | Value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 10  | 10  | ltn  | l  | mrr  | 0.48148148148148157  |
| 10  | 10  | ltn  | l  | map  | 0.46105820105820106  |
| 10  | 10  | ltn  | s  | mrr  | 0.48611111111111105  |
| 10  | 10  | ltn  | s  | map  | 0.47415498236331566  |
| 10  | 10  | lnn  | l  | mrr  | 0.13761904761904759  |
| 10  | 10  | lnn  | l  | map  | 0.20009920634920636  |
| 10  | 10  | lnn  | s  | mrr  | 0.21666666666666665  |
| 10  | 10  | lnn  | s  | map  | 0.22760912698412694  |
| 10  | 10  | nnn  | l  | mrr  | 0.16666666666666666  |
| 10  | 10  | nnn  | l  | map  | 0.07583333333333332  |
| 10  | 10  | nnn  | s  | mrr  | 0.05  |
| 10  | 10  | nnn  | s  | map  | 0.05583333333333333  |
| 10  | 10  | ntn  | l  | mrr  | 0.3387301587301587  |
| 10  | 10  | ntn  | l  | map  | 0.4988095238095238  |
| 10  | 10  | ntn  | s  | mrr  | 0.24166666666666664  |
| 10  | 10  | ntn  | s  | map  | 0.35867063492063483  |
| 10  | 10  | ltc  | l  | mrr  | 0.05095238095238095  |
| 10  | 10  | ltc  | l  | map  | 0.1328968253968254  |
| 10  | 10  | ltc  | s  | mrr  | 0.30625  |
| 10  | 10  | ltc  | s  | map  | 0.3052195767195767  |
| 10  | 10  | lnc  | l  | mrr  | 0.46333333333333326  |
| 10  | 10  | lnc  | l  | map  | 0.525  |
| 10  | 10  | lnc  | s  | mrr  | 0.425  |
| 10  | 10  | lnc  | s  | map  | 0.2876388888888889  |
| 10  | 10  | nnc  | l  | mrr  | 0.45833333333333337  |
| 10  | 10  | nnc  | l  | map  | 0.3405714285714285  |
| 10  | 10  | nnc  | s  | mrr  | 0.5604938271604938  |
| 10  | 10  | nnc  | s  | map  | 0.2191746031746032  |
| 10  | 10  | ntc  | l  | mrr  | 0.2222222222222222  |
| 10  | 10  | ntc  | l  | map  | 0.12611111111111112  |
| 10  | 10  | ntc  | s  | mrr  | 0.11527777777777777  |
| 10  | 10  | ntc  | s  | map  | 0.18472222222222223  |
| 1710  | 80  | ltn  | l  | mrr  | 0.5875854333569509  |
| 1710  | 80  | ltn  | l  | map  | 0.11062445268963234 |
| 1710  | 80  | ltn  | s  | mrr  | 0.557338925833172  |
| 1710  | 80  | ltn  | s  | map  | 0.08934026376611327  |
| 1710  | 80  | nnn  | l  | mrr  | 0.14837955654063983  |
| 1710  | 80  | nnn  | l  | map  | 0.026987730310542548 |
| 1710  | 80  | nnn  | s  | mrr  | 0.14317767301954462  |
| 1710  | 80  | nnn  | s  | map  | 0.030373320642299934  |
| 1710  | 80  | ltc  | l  | mrr  | 0.26845512297625423 |
| 1710  | 80  | ltc  | l  | map  | 0.04608079367437512  |
| 1710  | 80  | ltc  | s  | mrr  | 0.30332860620722135  |
| 1710  | 80  | ltc  | s  | map  | 0.0545965657015998 |
| 1710  | 80  | nnc  | l  | mrr  | 0.36605680269078483 |
| 1710  | 80  | nnc  | l  | map  | 0.05481614258081444 |
| 1710  | 80  | nnc  | s  | mrr  | 0.37505310232348865  |
| 1710  | 80  | nnc  | s  | map  | 0.05690836070725275  |


# Conclusion
From the results above, we can find a few conclusions:

1. ‘nnn’ returns the lowest metric of all scoring schemes, regardless of the method used, number of queries and documents provided to evaluation.py and query.py.
2. Stemming, generally, provides a higher/better metric than lemmatization across all test cases.
3. With an increase in the number of documents or queries, the difference in value between MRR and MAP metrics increases, regardless of the scoring scheme or method used. They are inversely proportional. That is, MAP decreases with an increase in the number of documents or queries, whereas MRR stays relatively similar with slight differences.
4. For the same number of documents and queries, ’ltc’ (cosine normalized ‘ltn’) scheme returns lower MRR and MAP values in comparison to ‘ltn’. However, ‘nnc’ (cosine normalized ‘nnn’) yields higher/better MRR and MAP scores than ‘nnn’ scoring scheme.

# Best Set of Parameters (based on this experiment)
Based on this, we can provide a balanced set of parameters for a command line argument [NOTE: Number of documents retrieved and randomized queries can be changed] :
-> Scoring Scheme: 'ltn'
-> Method: 's' (Stemming)
-> Metric: 'mrr' (Mean Reciprocal Rank)
```python3 ./code/evaluation.py CISI_simplified ltn s 10 10 mrr``` 
