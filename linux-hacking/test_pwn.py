from pwn import *
print(cyclic(50))
print(cyclic_find("laaa"))

"""
#interact with shell on local
p = process("/bin/sh")
p.sendline("echo hello;")
p.interactive()
"""
"""
#remote to other server
r = remote("127.0.0.1",1234)
r.sendline("hello")
r.interactive()
r.close()
"""

print(xor(xor("A","B"),"A"))
#encode base64
print(b64e(b"test"))
#decode base64
print(b64d(b"dGVzdA=="))
print(md5sumhex(b"hello"))
print(sha1sumhex(b"hello"))
print(bits(b"a"))
print(unbits([0, 1, 1, 0, 0, 0, 0, 1]
)) 