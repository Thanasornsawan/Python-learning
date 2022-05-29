tuple_item = ("item1","item2","item3")
print(tuple_item)

tuple_number = (1,2,3)
print(tuple_number)

tuple_repeat = ('Combine!,') * 4
print(tuple_repeat)

mixed_tuple = ("A", 1, ("A",1))
print(mixed_tuple)
#tuple can't change, can't append to the existing data, only combined

combined_tuple = tuple_item + tuple_number
print(combined_tuple)

#we can assign to muitple variable
item1, item2, item3 = tuple_item
print(item1)

print("item2" in tuple_item)
print(tuple_item.index("item2"))
print(tuple_item[2])
print(tuple_item[-1]) #get the last element

print(tuple_item[0:2])
print(tuple_item[:2])
print(tuple_item[-3:-1]) #print index from last