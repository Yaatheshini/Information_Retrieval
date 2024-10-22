'''
Generalizes the output of print_query.py from documents 1-20 of CISI
'''
import random
import subprocess

print("Testing output of print_query -- expected to PASS")
correct_queries = {}

correct_queries["1"] = "What problems and concerns are there in making up descriptive titles?" \
" What difficulties are involved in automatically retrieving articles from" \
" approximate titles?" \
" What is the usual relevance of the content of articles to their titles?"

correct_queries["2"] = "How can actually pertinent data, as opposed to references or entire articles" \
" themselves, be retrieved automatically in response to information requests?"

correct_queries["3"] = "What is information science?  Give definitions where possible."

correct_queries["4"] = "Image recognition and any other methods of automatically" \
" transforming printed text into computer-ready form."

correct_queries["5"] = "What special training will ordinary researchers and businessmen need for proper" \
" information management and unobstructed use of information retrieval systems?" \
" What problems are they likely to encounter?"

correct_queries["6"] = "What possibilities are there for verbal communication between computers and" \
" humans, that is, communication via the spoken word?"

correct_queries["7"] = "Describe presently working and planned systems for publishing and printing" \
" original papers by computer, and then saving the byproduct, articles coded in" \
" data-processing form, for further use in retrieval."

correct_queries["8"] = "Describe information retrieval and indexing in other languages." \
" What bearing does it have on the science in general?"

correct_queries["9"] = "What possibilities are there for automatic grammatical and contextual analysis" \
" of articles for inclusion in an information retrieval system?"

correct_queries["10"] = "The use of abstract mathematics in information retrieval, e.g. group theory."

correct_queries["11"] = "What is the need for information consolidation, evaluation, and retrieval in" \
" scientific research?"

correct_queries["12"] = "Give methods for high speed publication, printing, and distribution of" \
" scientific journals."

correct_queries["13"] = "What criteria have been developed for the objective evaluation of information" \
" retrieval and dissemination systems?"

correct_queries["14"] = "What future is there for automatic medical diagnosis?"

correct_queries["15"] = "How much do information retrieval and dissemination systems, as well as" \
" automated libraries, cost?" \
" Are they worth it to the researcher and to industry?"

correct_queries["16"] = "What systems incorporate multiprogramming or remote stations in information" \
" retrieval?  What will be the extent of their use in the future?"

correct_queries["17"] = "Means of obtaining large volume, high speed, customer usable" \
" information retrieval output."

correct_queries["18"] = "What methods are there for encoding, automatically matching," \
" and automatically drawing structures extended in two dimensions," \
" like the structural formulas for chemical compounds?"

correct_queries["19"] = "Techniques of machine matching and machine searching systems." \
" Coding and matching methods."

correct_queries["20"] = "Testing automated information systems."

program = "./code/print_query.py"
collection = "CISI"
queryID = str(random.randint(1, 20))

print("Query generated is: ", queryID)

output = subprocess.check_output(["python3", program, collection, queryID])
answer = output.decode('utf-8').strip()

# compare outputs, word by word
words_answer = answer.split()
words_query = correct_queries[queryID].strip().split()

if len(words_query) == len(words_answer):
    for i in range(len(words_answer)):
        if words_query[i] != words_answer[i]:
            print("FAIL: The text words don't match.")
            exit(1) # signal error to OS

    # if we reach this point, the answer is correct
    print("PASS")
    exit(0) # signal success to OS

# if we reach this point, the returned answer is not as expected
print("FAIL: The number of words in the text doesn't match.")
exit(1) # signal error to OS