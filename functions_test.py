def function1():
    print("Hello from function!")

function1()

def function2():
    return "Hello from function2!"
    
return_from_function2 = function2()
print(return_from_function2)

def function3(s):
    print("\t{}".format(s))
    
function3("parameter")

def function4(s1,s2):
    print("{} {}".format(s1,s2))
    
function4("any", "thing")
function4(s2="thing",s1="any")

def function5(s1="default"):
    print("{}".format(s1))

function5()

#for unknow amount of input can use *more 
def function6(s1, *more):
    print("{} {}".format(s1, " ".join([s for s in more])))
    
function6("function6", "a", "b", "c")

#get value as dictionary and it can be any length
def function7(**ks):
    for a in ks:
        print(a, ks[a])
        
function7(a="1",b="2",c="3")

v=100
def function9():
    global v
    v+=1 
    print(v)

function9()

#recursive function call function itself
def function10(x):
    print(x)
    if x>0:
        function10(x-1)
        
function10(5)

def function11(x):
    while x>=0:
        print(x)
        x-=1
function11(5)