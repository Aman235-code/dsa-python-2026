from array import *

val = array('i',[1,2,3,4,5,6,7,8,9])

i = val.index(5)

print(i)

# for i in range(0, len(val)):
#     print(val[i], end=" ")

# print("\n")

# for x in val:
#     print(x, end=",")

# print(val.typecode)
# val.reverse()

# for i in val:
#     print(i, end=" ")

# val.insert(1, 50) # inserting at position
# val.append(100) # added at last 
# val[2] = 200 # replace
# for i in val:
#     print(i, end=" ")

# copyArray = array(val.typecode, (x for x in val))
# copyArray.pop() # index # no index last element
# copyArray.remove(1) # element 
# for i in copyArray:
#     print(i, end=" ")

# a = val[2:5]
# a = val[2: -3]
# a = val[::-1]
# for i in a:
#     print(i, end=" ")

# arr = array('i',[])
# n = int(input("Enter a number"))

# for i in range(0, n):
#     arr.append(int(input('Enter next input')))

# for x in arr:
#     print(x, end=" ")