from Nested_dict import complex_nested_dict

for item, value in complex_nested_dict.items():
    for company, title in value.items():
        print(company, "\n", title, "\n", "\n")