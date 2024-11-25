import requests
import json

url = "https://raw.githubusercontent.com/DesayoEm/datasets/refs/heads/main/practice.json"
response = requests.get(url)
data=response.json()


# print(data)
# # data.update({1:"你好，世界!"})


# with open ('xfile.json', 'w', encoding ='utf-8') as vfile:
#     json.dump(data, vfile,indent = 4, ensure_ascii=False)

# # # str='{"1":"你好，世界!"}'

# # # dd=json.loads(str)
# # # print(str)
# # # print(type(dd))
                       
# with open('xfile.json', 'r', encoding='utf=8') as jubjub:
#     myd=json.load(jubjub)

# # print (myd)
# # print(type(myd))
# # for k, v in myd.items():
# #     (print(k, v))

# print(myd["people"]["Akua Boateng"])
# myd.update({2: "supsup"})

# with open ('xfile.json', 'w') as jubjub:
#     json.dump(myd, jubjub, indent =4)

emp={}
with open ('pipe.txt', 'r') as supsup:
    supsup.readline()
    for line in supsup:
        data=line.strip().split("|")
        # print (data)
        no, name, age, email, city = data
        mudict={
            "name":name,
            "age":age,
            "email":email,
            "city":city
        }
        emp[no] = mudict

for id, value in emp.items():
    print(id, value)