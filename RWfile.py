f=open('top-100.txt','rt')
print(f.read())
print(f.readlines()) #contain line\n, show output as array
#if we use readlines() again,it will show empty array.We need to use f.seek(0) to start from beginning
f.seek(0)
print(f.readlines())
for line in f:
    print(line.strip())
f.close()

#open and write file (overwritten)
f=open('test.txt','w')
f.write("test line")
f.close()
#not overwritten file but append text in file
f=open('text.txt','a')
f.write("test line2")
f.close()

print(f.name()) #text.txt
print(f.closed()) #true
print(f.mode()) #a 

print("----------------")
with open('rockyou.txt', encoding='latin-1') as f:
    for line in f:
        pass