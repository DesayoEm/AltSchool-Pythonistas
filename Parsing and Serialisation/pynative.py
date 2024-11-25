import json
from pprint import pprint
# Exercise 1: Convert the following dictionary into JSON format
# data = {"key1" : "value1", "key2" : "value2"}
# data=json.dumps(data)
# print(type(data))

# Exercise 2: Access the value of key2 from the following JSON
# sampleJson = """{"key1": "value1", "key2": "value2"}"""
# data=json.loads(sampleJson)
# print(data["key2"])


# Exercise 3: PrettyPrint following JSON data
# PrettyPrint following JSON data with indent level 2 and key-value separators should be
#  (",", " = ").

sampleJson = {"key1": "value1", "key2": "value2"}
pprint(json.dumps(sampleJson))
