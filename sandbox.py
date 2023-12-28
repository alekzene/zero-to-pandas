# test
i = 2
if (i == 2):
  print(2)

# random thought: can i use !<= to say "not less than or equal to"?
# i know it's inconvenient and we can just use >
# i just got curious
  
# if (i !<= 1):
#   print(1)

# ok... we can't

""" multi-line comment """

is_true = True # note: true is not defined in Python; use True

# Why do we use Jupyter Notebook? What is the value it offers to the data science and computer science community?

# multi-assignment
var1, var2, var3, var4 = "mama", "papa", "ate", "kuya"
# adding another value at the end results in ValueError: too many values to unpack (expected 4)

print(var1)
print(var2)
print(var3)
print(var4)

# chaining
var1 = var2 = var3 = "chikana"

print(var1)
print(var2)
print(var3)
print(var4)

# idk what to call this
num = 1
num += 2 # increment by 2
print(num)
num -= 3 # decrement by 3
print(num)
num *= 4 # idk what to call this (2)
print(num)
num /= 5 # idk what to call this (3)
print(num)