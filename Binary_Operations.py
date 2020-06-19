x = int(input("x:"))
mask = 0b000000001
k = int(input("k:"))
mask <<= k-1


#check if k-th bit is 0 or 1
if (x & mask):
    print("is set")
else : print("isnt set")


#set kth bit
y = bin(x | mask) 


#unset kth bit
y = bin(x & (~mask))


#toggle the k-th bit
y = bin(x ^ mask)


#toggle right most set bit
y = bin(x & (x-1))


# finding no.of 1's
count = 0
while(x):
    count += int(x & 1)
    x = x>>1
print(count)


#isolating rmb
print(bin(x & -x))      # -x is 2's compliment of x


#checking if number is a power of 2
if (x & (x-1)):
    print("not power of 2")
else: print("power of 2")
