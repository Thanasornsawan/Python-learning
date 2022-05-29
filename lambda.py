#lambda is function

add_4 = lambda x : x+4 
print(add_4(4))

add = lambda x,y: x+y 
print(add(10,4))

print((lambda x,y : x+y )(10,4))

is_even = lambda x: x%2 == 0 
print(is_even(2))
print(is_even(3))

blocks = lambda x,y : [x[i:i+y] for i in range(0, len(x),y)]
print(blocks("string",2)) #break input into two chars

#ord return unicode
to_ord = lambda x: [ord(i) for i in x]
print(to_ord("ABCD"))

def to_ord2(x):
    ret=[]
    for i in x:
        ret.append(ord(i))
    return ret 
    
print(to_ord2("ABCD"))