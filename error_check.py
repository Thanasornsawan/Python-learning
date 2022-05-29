try:
    abc
    f=open("testttttt")
except FileNotFoundError:
    print("The file does not exist")
except Exception as e:
    print(e)
finally:
    print("This message!")
    
print("-------")

n=100
if n==0:
    raise Exception("n can't be 0!")
if type(n) is not int:
    raise Exception("n must be an int!")
print(1/n)

print("-------")
n=0
assert(n!=0)
print(1/n)