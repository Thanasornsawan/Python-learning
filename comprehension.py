list1 = ["a","b","c"]
print(list1)

list2 = [x for x in list1]
print(list2)

list3 = [x for x in list1 if x=="a"]
print(list3)

list4 = [x for x in range(5)]
print(list4)

list5 = [hex(x) for x in range(5)]
print(list5)

list6 = [hex(x) if x>0 else "X" for x in range(5)]
print(list6)

list7 = [x * x for x in range(5)]
print(list7)

list8 = [x for x in range(5) if x==0 or x==1]
print(list8)

list9 = [c for c in "string"]
print(list9)

print("".join(list9))

list10 = []
for c in "string":
    list10.append(c)
print(list10)

list11 = [[1,2,3],[4,5,6],[7,8,9]]
list12 = [y for x in list11 for y in x]
print(list12)