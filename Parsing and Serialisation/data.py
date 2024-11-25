from pprint import pprint

data_list=[]
data_dict={}
with open ('pipe.txt', 'r') as file:
    file.readline()
    for line in file:
        datax=line.strip().split("|")
        no, name, age, email, city = datax
        # data_list.append(datax)
        my_dict={
            "name":name,
            "age":age,
            "email":email,
            "city":city
        }
        data_dict[no]=my_dict


# # pprint(data_dict)
# del [data_dict["id"]]

for id, value in data_dict.items():
    print(id, value)
        
# for itrm in data_list:
#     print(itrm)