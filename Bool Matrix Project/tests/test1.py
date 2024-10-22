import ast
import subprocess

program = "./code/build_matrix.py"
collection = "good"

output = subprocess.check_output(["python3", program, collection])

file = open("./processed/good.matrix.json", 'r')
lines = file.read()
matrix = ast.literal_eval(lines) 

matrix_hc = {
    "_M_": 5,
    "1": [1, 0, 0, 0, 0],
    "15l": [0, 0, 0, 1, 0],
    "361": [1, 0, 0, 0, 0],
    "a": [0, 0, 0, 1, 0],
    "and": [0, 1, 0, 0, 0],
    "assign": [1, 0, 0, 0, 0],
    "atleast": [0, 0, 0, 1, 0],
    "be": [0, 1, 0, 0, 0],
    "case": [1, 0, 0, 0, 0],
    "cmput": [1, 0, 0, 0, 0],
    "day": [0, 0, 0, 1, 0],
    "debug": [0, 0, 1, 0, 0],
    "document": [0, 0, 0, 0, 1],
    "drink": [0, 0, 0, 1, 0],
    "essenti": [0, 0, 0, 1, 0],
    "everyth": [0, 1, 0, 0, 0],
    "final": [0, 0, 0, 0, 1],
    "golden": [0, 1, 0, 0, 0],
    "good": [1, 1, 0, 0, 0],
    "goodby": [0, 0, 0, 0, 1],
    "here": [0, 1, 0, 0, 0],
    "in": [0, 0, 0, 1, 0],
    "includ": [0, 0, 1, 0, 0],
    "is": [1, 0, 0, 1, 1],
    "must": [0, 0, 1, 0, 0],
    "of": [1, 0, 1, 1, 0],
    "plenti": [0, 0, 1, 0, 0],
    "should": [0, 1, 0, 0, 0],
    "strategi": [0, 0, 1, 0, 0],
    "test": [0, 0, 1, 0, 0],
    "the": [1, 0, 0, 0, 1],
    "thi": [1, 0, 0, 0, 1],
    "water": [0, 0, 0, 1, 0],
}

if matrix == matrix_hc:
    print("PASS")
    exit(0)
else:
    print("FAIL")
    exit(1)