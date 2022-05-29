#set can't order, no index, can't duplicate value
set1 = {"a","b","c"}
print(set1)

set2 = {"a","a","a"}

set3 = {"a",0,True}

set4 = set(("b",1,False))
print(set4)

set1.add("d")
print(set1)

set3.update(set4)
print(set3)
#we can update set with different kind of itterable
list1 = ["a", "b", "c"]

set4 = {4,5,6}
set4.update(list1)
print(set4)

set5 = {4,5,6}
set6 = set4.union(set5)
print(set6)

set4.remove(4)
print(set4)

set4.discard(4) #same remove but if use remove again it will error 
print(set4)

#avoid to use .pop with set because set not have order
