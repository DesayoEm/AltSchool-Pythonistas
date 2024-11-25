# import requests
import json
from pprint import pprint

# url = "https://raw.githubusercontent.com/DesayoEm/datasets/refs/heads/main/practice.json"
# my_json=requests.get(url)
# data = my_json.json()

# data.update({1: "你好，世界！"})

# # pprint(data)
# with open('data.json', 'w', encoding='utf-8') as my_file:
#     json.dump(data, my_file, indent=4, ensure_ascii=False)

# for id, value in data.items():
#     pprint(id, value)

# print(data["people"]["Tunde Adebayo"])


# def write_file(data):
#     with open('newfile.json', 'w') as tiptop:
#         json.dump(data, tiptop, indent=4)


# with open ('data.json', 'r') as taptap:
#     new_data=json.load(taptap)

# new_data["people"]["Kwame Mensah"]["nationality"] = "Nigerian"
# write_file(new_data)

#JSON does not have a representation of a tuple

my_tuple = (
    ("Alice", 30, "New York"),
    ("Bob", 25, "Los Angeles"),
    ("Charlie", 35, "Chicago")
)
print(type(my_tuple))


jstuple=json.dumps(my_tuple)
print(type(jstuple))

jstuplelist=json.loads(jstuple)
print(type(jstuplelist))
print(jstuplelist[1])
