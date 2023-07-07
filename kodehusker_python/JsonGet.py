import json
import os

cwd = os.getcwd()


class passObj:
    def __init__(self, place, user, password):
        self.place = place
        self.user = user
        self.password = password

    def __str__(self):
        return f"passObj: {self.place}, {self.user}, {self.password}"


obj_list = []

file_path = os.path.join(cwd, 'kodehusker_python', 'save.json')


try:
    with open(file_path, "r") as f:
        data = json.load(f)

    for item in data:
        obj = passObj(item['place'], item['user'], item['password'])
        obj_list.append(obj)


except FileNotFoundError:
    print(f"File not found: {file_path}")

except json.JSONDecodeError:
    print(f"Error decoding JSON file: {file_path}")

print(obj_list)