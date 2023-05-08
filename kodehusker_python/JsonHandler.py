import json
import os
cwd = os.getcwd()

class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

s1 = Student('john', 4)
s2 = Student('Sunil', 6)
s3 = Student('joghd', 7)

myList = [s1, s2, s3]

json_object = json.dumps([obj.__dict__ for obj in myList])
print(json_object)

with open(cwd + '\kodehusker_python\save.json', "w") as outfile:
    outfile.write(json_object)