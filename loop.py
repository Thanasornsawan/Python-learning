a=1
while a < 5:
    a+=1
    print(a)
print("for")
for i in [0,1,2,3,4]:
    print(i+6)
print("- 1---")
for i in range(5):
    print(i+6)
print("- 2---")
for i in range(5):
    if i == 2:
        break
    print(i)
print("- 3---")  
for i in range(5):
    if i == 2:
        continue
    print(i)
print("- 4---")
for c in "string":
    print(c)
print("- 5---")
for key,value in {"a":1,"b":2,"c":3}.items():
    print(key,value)
print("- 6---")
