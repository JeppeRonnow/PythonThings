import json
import os
cwd = os.getcwd()

with open(cwd + '\kodehusker_python\save.json', "r") as f: 
    myList = json.load(f)

print(myList)