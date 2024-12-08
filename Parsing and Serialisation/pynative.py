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

# sampleJson = {"key1": "value1", "key2": "value2"}
# pprint(json.dumps(sampleJson))

# Exercise 4: Sort JSON keys in and write them into a file
# Sort following JSON data alphabetical order of keys

# sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

# with open ("samplejson.json", 'w') as jubjub:
#     json.dump(sampleJson, jubjub, indent=2, ensure_ascii=False, sort_keys=True)


# Exercise 5: Access the nested key ‘salary’ from the following JSON

# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payble":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""

# new_json=json.loads(sampleJson)
# print(new_json["company"]["employee"]["payble"]["salary"])

# Exercise 6: Convert the following Vehicle Object into JSON

# SOLUTION 1
# class Vehicle:
#     def __init__(self, name, engine, price):
#         self.name = name
#         self.engine = engine
#         self.price = price
    
#     def serialiser(self):
#         return{"name":self.name, "engine":self.engine, "price": self.price}
    

# toyota= Vehicle("Toyota Rav4","2.5L",32000 )
# # print(toyota.__dict__)
# json_toyota=(json.dumps(toyota.__dict__, indent = 4))
# print(json_toyota)



# print(json_toyota)

# # vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

#SOLUTION 2
# from json import JSONEncoder

# class Vehicle:
#     def __init__(self, name, engine, price):
#         self.name = name
#         self.engine = engine
#         self.price = price

# class VehicleEncoder(JSONEncoder):
#         def default(self, o):
#             return o.__dict__

# vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

# print("Encode Vehicle Object into JSON")
# vehicleJson = json.dumps(vehicle, indent=4, cls=VehicleEncoder)
# print(vehicleJson)




# Convert the following JSON into Vehicle Object

# json_x='{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }'
# json_dict=json.loads(json_x)
# # print(type(json_dict))

# class Vehicle:
#     def __init__(self, name, engine, price):
#         self.name = name
#         self.engine = engine
#         self.price = price

#     def __str__(self):
#         return f"Vehicle(name='{self.name}', engine='{self.engine}', price={self.price})" 


# vehicle=Vehicle(**json_dict)
# print(vehicle)
# print(type(vehicle))

# # print(vehicle.__dict__)
# # print(type(vehicle))



# print(vehicle)
# print(vehicle_json)


# InvalidJsonData = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000  "bonus":800} } } }"""

# def validate(data):
#     try:
#         json.loads(data)
#     except ValueError as e:
#         return False
#     return True

# print (validate(InvalidJsonData))



# Exercise 9: Parse the following JSON to get all the values of a key ‘name’ within an array
lis="""[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""
# lis=json.loads(lis)

# lst = []
# for item in lis:
#     lst.append(item["name"])
# print(lst)


# dataList = [item.get('name') for item in lst]

x={ 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }

# var=x.pop("id")

x["nameb"]=x.pop("id")

x["namec"]="erfewwew"
print(x)


# users[update_profile.username] = users.pop(Id) 
# # user_data["username"] = update_profile.username
