from Nested_dict import complex_nested_dict

# 1.Retrieve the name of the first ongoing project that Bob is working on.
# SOLUTION 1
# if "company" in complex_nested_dict and "employees" in complex_nested_dict["company"]:
#     for employee in complex_nested_dict["company"]["employees"]:
#         if employee["name"] == "Bob" and "projects" in employee:
#             ongoing_projects = employee["projects"].get("ongoing", [])
#             first_ongoing_project = ongoing_projects[0] if ongoing_projects else None
#             print(f"The first project Bob is working on is {first_ongoing_project}")
#             break 

# SOLUTION2
# print(complex_nested_dict["company"]["employees"][1]["projects"]["ongoing"][0]) 

#SOLUTION 3
# print(complex_nested_dict.get("company").get("employees")[1].get("projects").get("ongoing")[0])

# SOLUTION 4
# find_bob=complex_nested_dict["company"]["employees"]
# for person in find_bob:
#     if person["name"]=="Bob":
#         print(person["projects"]["ongoing"][0])



# 2.Find the street address of the company.
# SOLUTION 1
# print(f"The street address is {complex_nested_dict["company"]["location"]["address"]["street"]}")

#SOLUTION2
# x = complex_nested_dict.get("company").get("location").get("address").get("street")
# print(x) 

# 3.Access the role of the second employee listed in the employees list.
#SOLUTION 1
# print(f"The role of the second employee is {complex_nested_dict.get("company").get("employees")[1].get("role")}")

#SOLUTION 2
# print(f"The role of the second employee is {complex_nested_dict["company"]["employees"][1]["role"]}")


# 4.Get the name of the team lead for the development department.
# SOLUTION 1- Aaminah
# print(f"The name of the team lead for the development department is {complex_nested_dict["company"]["departments"]["development"]["team_lead"]}") 
# SOLUTION 2- ISSAC
# print(complex_nested_dict.get("company").get("departments").get("development").get("team_lead")) 


# 5.Identify the first skill of the employee named Alice.
# x = complex_nested_dict.get("company").get("employees")[0].get("skills")[0]
# print(f"The first skill of the employee named Alice is {x}") 



# 11.Extract the names of all employees who have "Python" as a skill.
# for employee in complex_nested_dict.get("company").get("employees"):
#     for skill in employee.get("skills"):
#         if skill == "Python":
#             print(employee.get("name"))
        

# 12.Find the name of the partner company that provides "Fraud Detection" as a service.
# for partners in complex_nested_dict.get("company").get("partnerships"):
#     if "Fraud Detection" in partners.get("services"):
#         print(partners.get("partner_name"))
    
    

# 13.Access the list of all skills that employees have, without any duplicates.
# print(complex_nested_dict.get("company").get("employees")[0].get("skills"))
# print(complex_nested_dict.get("company").get("employees")[1].get("skills"))

# SOLUTION 1
# skills = []
# for employee in complex_nested_dict.get("company").get("employees"):
#     for skill in employee.get("skills"):
#         if skill not in skills:
#             skills.append(skill)
# print(skills) 

# SOLUTION2
# people=complex_nested_dict["company"]["employees"]
# skills=[]

# for employee in people:
#     for skill in employee["skills"]:
#         skills.append(skill)

# skills=set(skills)
# skills=list(skills)

# print(skills)

# SOLUTION 3
# people=complex_nested_dict["company"]["employees"]
# print(list({skill for person in people for skill in person["skills"]}))

# 14. Retrieve the names of all ongoing projects across all employees in a single list.

# ongoing_projects = []
# for employee in complex_nested_dict.get("company").get("employees"):
#     ongoing_projects.extend(employee.get("projects").get("ongoing"))
# print(ongoing_projects) 

# 15.Calculate the total budget for both the development and marketing departments combined.

#SOLUTION 1     
# store = complex_nested_dict["company"]["departments"]
# print(store["development"]["budget"] + store["marketing"]["budget"]) 

#SOLUTION 2
# total_budget = complex_nested_dict.get("company").get("departments").get(
#     "development"
# ).get("budget") + complex_nested_dict.get("company").get("departments").get(
#     "marketing"
# ).get(
#     "budget"
# )
# print(total_budget) 

#SOLUTION 3
# total_budget = sum(
#     [
#         complex_nested_dict.get("company")
#         .get("departments")
#         .get("development")
#         .get("budget"),
#         complex_nested_dict.get("company")
#         .get("departments")
#         .get("marketing")
#         .get("budget"),
#     ]
# )
# print(total_budget) 

#SOLUTION 4
# total=0
# store = complex_nested_dict["company"]["departments"]

# for dept, value in store.items():
#     total+=value['budget']
# print(total)
