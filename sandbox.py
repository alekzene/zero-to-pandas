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
print(num) # turned into a float bc got divided [div (/) always returns float]
# use floor division (//) to keep int

# var names cannot start with numbers
# 3_muskateers = 123 # SyntaxError: invalid decimal literal

print(type(num))

random = 2.3487484778785787878578585
num = -892839893889289392998238928939823892893239238223 # int & float datatyped in python have no value limits

num =  2. # no syntax error if i put a dot at the end of a numerical value; auto counts as float

# FIXME review scientific notation (with 'e')
one_hundredth = 1e-2
avogadro_number = 6.02214076e23 

# casting
avogadro_number = int(avogadro_number) # float --> int removes decimals
print(avogadro_number)

""" Python : Java 
list : list
tuple : enum
dictionary : hashmap """