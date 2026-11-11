schooldata={"id1":{"name":"Nathan","Age":"15","Grade":10,"Subject":"Coding"},
            "id2":{"name":"Ben","Age":"12","Grade":7,"Subject":"English"},
            "id3":{"name":"Tina","Age":"9","Grade":4,"Subject":"Math"},
            "id4":{"name":"Nathan","Age":"15","Grade":10,"Subject":"Coding"}}
seen=[]
result={}
for id, details, in schooldata.items():
    unique_key=(details["name"],details["Subject"],details["Grade"])

    if unique_key not in seen:
        result[id]=details
        seen.append(unique_key)

for key,value in result.items():
    print(key,":",value)
