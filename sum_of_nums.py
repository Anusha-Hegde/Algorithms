'''
given 2 lists of int elements, a and b, both are added as if they are one element. Implementation using stack.

Example: 
a = [1, 2, 3]
b = [1, 2, 3, 4]

output = 2464 (123 + 1234)
'''
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
carry = 0
if len(a)>len(b):
    while len(a) != len(b): 
        c.append(str(a.pop(-1)))
elif len(a) < len(b):
    while len(a) != len(b): 
        c.append(str(b.pop(-1)))
while len(a):
    add = a.pop(-1) + b.pop(-1) + carry
    if add > 9:
        c.append(str(add - 10))
        carry = 1
    else:
        c.append(str(add))
        carry = 0
c = reversed(c)
c = ''.join(c)
print(c)