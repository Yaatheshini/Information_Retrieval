import subprocess

program = "./code/query.py"
collection = "good"

file = open("./collections/good.QRY", 'r')
file1 = open("./collections/good.REL", 'r')

temp = ''
results = {}
for line in file1.readlines():
    line = line.split()
    if line[0] not in results.keys():
        results[line[0]] = []

    results[line[0]].append(int(line[1]))

condition = True
for line in file.readlines():
    if line[0:2] == '.I':
        line = line.split()
        temp = line[1]
        continue

    output = subprocess.check_output(["python3", program, collection, line.strip()])
    output = output.decode('utf-8').strip()

    temp1 = results[temp][0]
    if output == temp1:
        condition = False
        break
    print("A")
if condition:
    print("PASS")
    exit(0)

else:
    print("FAIL")
    exit(1)




    
