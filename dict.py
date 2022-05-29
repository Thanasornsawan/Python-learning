dict1 = {"a":1, "b":2, "c":3}
print(dict1)

print(dict1["a"])
print(dict1.get("a"))
print(dict1.keys())
print(dict1.values())
print(dict1.items())
#change value of the key
dict1["a"] = 0
#add new dict
dict1["d"] =4
print(dict1)
#update value of key
dict1.update({"a":2})
print(dict1)

dict1.pop("d")
print(dict1)

del dict1["c"]
print(dict1)

dict1["d"] = {"a":1,"b":2}
print(dict1)

dict2 = {}
print(dict2)

dict3 = dict() #empty dictionary
print(dict3)