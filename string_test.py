multiline_str = """ I am 
a very 
long string """

multiline_num = 1+2\
    +3
print(multiline_str)
print(multiline_num)

add_quote = "I' am str"
print(add_quote)
add_quote2 = "I\" am str2\n yes"
print(add_quote2)
hex_data = "\\ \x41\x42\x43"
print(hex_data)
ten_a = "a" * 10
print(ten_a)
#looking for word in sentence
print("am" in add_quote)
print(add_quote.startswith("I"))
print(add_quote.index("str"))
print(add_quote.upper())
print(add_quote.lower())
messy_string = " Messy string! "
print(messy_string.strip())
print(messy_string.replace("!","?").strip())
print(add_quote.rjust(25))
print(add_quote.rjust(25,"X"))
print(add_quote.ljust(25))

print("string4 is {} character long!".format(len(add_quote)))
print("{} {} {}".format(len(add_quote), 5.0, 0x12))
print("{0} {2} {1}".format(len(add_quote), 5.0, 0x12)) #specify order of the string with format
print("{length}".format(length=len(add_quote)))
#we can use f instread of use full "format"
length = len(add_quote)
print(f"string4 is {length} character long")
print(f"string4 is {length:.2f} character long")
print(f"string4 is {length: 3f} character long")
print(f"string4 is {length:o} character long")
print("string4 is %d characters long!" % length)
print("string4 is %f characters long!" % length)
print("string4 is %x characters long!" % length)

x=13
print(bin(x))
print(bin(x)[2:].rjust(4,"0")) # [2:0] is remove 2 bits at front
y=5
print(bin(y)[2:].rjust(4,"0"))

print(add_quote[0:4])
print(add_quote[-1]) #print last index