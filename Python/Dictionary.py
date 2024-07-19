info = {
    "name" : "Naman",
    "name" : "Naman",
    "key": "value",
    "list": [1,2,3,4],
    "tupple": (1,"dfs", 7,),
    "age" : 35,
    False: True,
    (1,2,3) : [1,2,3,4,5],
    None : "none datatype"
}

\
info["age"] = [2,3,4]
info["surname"] = "Gujartathi"
print(info["age"])
print(info)

null_dict = {}

print("null_dict" , null_dict)

null_dict["name"] = "sam"

print(null_dict)


student = {
    "rollNo.1" : {
                    "Subjects": {
                        "Physics" : 90,
                        "Maths": 100
                    },
                    "School": "Xavier"
                   },
     "rollNo.2" : {
                    "Subjects": {
                        "Physics" : 70,
                        "Maths": 60
                    },
                    "School": "Sam"
                   }
    
}

print(type(student))
print(student.values())
print(len(student.keys()))
list1 = list(student.items())
print("get", student.get("rollNo.1"))

new_dict = {"city" : "Indore", "age" : 60, 60: "dhsd"}
student.update(new_dict)
print("updated", student)