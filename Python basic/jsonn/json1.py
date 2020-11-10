import json

person_dict={"name":"arjun","language":["english","hindi"],"age":22}
print(type(person_dict))
print("__________________")
person_json=json.dumps(person_dict)
print(type(person_json))

with open("persn.txt","w") as json_file:
    json.dump(person_json,json_file)

with open("person.txt","r") as json_file:
    print(json.load(json_file))