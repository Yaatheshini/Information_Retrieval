import ast
import subprocess

program = "./code/query.py"
collection = "good"
file = open("./collections/good.QRY", 'r')

invalid_queries = ["( ground :and: plant ) :and: :not: sun","( ground :and: plant :and: :not: sun )","(ground:and:plant):and::not:sun","(and:plant):and:sun","(ground:and:plant):and:sun:or:"]
 
for query in invalid_queries:
    output = subprocess.check_output(["python3", program, collection, query])
    if output != 0:
        print(f"Failed Case {invalid_queries.index(query)}")
    else:
        print(f"Passed Case {invalid_queries.index(query)}")