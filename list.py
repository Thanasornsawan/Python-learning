list1 = ["A", "B", "C", "D", "E", "F"]
print(list1)
list2 = ["A", 1, 2.0,["A"],[],list(),("A"), False ]
print(list2)
print(list1[0])
print(list1[-1])
print(list2[3][0]) #print index of list in list
#list index canbe change
list1[0] = "X"
print(list1)
#delete index
del list1[0]
print(list1)

list1.insert(0,"A")
print(list1)

list1 = ["X"] + list1
print(list1) 

list1.append("G")
print(list1)

print(max(list1))
print(min(list1))

print(list1.index("C"))
#To verify that this index found in list
print(list1[list1.index("C")])
list1.reverse()
print(list1)

list1 = list1[::-1]
print(list1)

print(list1.count("A"))

#remove last index by pop
list1.pop()
print(list1)

list3 = ["H", "I", "J"]
list1.extend(list3)
print(list1)

#remove all value in the list
list1.clear()
print(list1)

list4 = [8,12,5,6,17,2]
list4.sort()
print(list4)

list4.sort(reverse=True)
print(list4)

#copy element in list cannot assign by = because whenever another list change
#the original list also change.It point to the same place

list5 = list4
list5[2] = "X"
print(list5)
print(list4)
#but if use function copy,it will not effect to the original list
list6 = list4.copy()
list6[2] = "A"
print(list6)
print(list4)

#use map when want to apply some function to all list
list7 = [1,2,3]
print(list7)
list8 = list(map(float,list7))
print(list8)

