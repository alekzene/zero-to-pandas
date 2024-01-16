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

# boolean (type: bool)
# all values are truthy except for 0, 0.0, None, and empty data structures(list, tuple, dict, set) and ranges

# strings (type: string)
# interestingly, in Jupyter Hub, the output includes single quotations (') enclosing the string value
# however, in VSCode, the output doesn't have any quotation marks. why so?
# ANSWER: in Jupyter Hub, the variable was called and its output was produced. no print function used.
# in VSCode, i used the print() function to display the output, which automatically removes the quotation marks.
print("Saturday")

# in Jupyter Hub, if the string value uses a single quotation mark in the string literal,
# the output automatically uses double quotation marks (") for enclosure

# to use a double quote within a string written with double quotes, 
# escape the inner quotes by prefixing them with the `\` character
another_pun = "The first time I got a universal remote control, I thought to myself \"This changes everything\"."

# multiline quotes
""" Python : Java 
list : list
tuple : enum
dictionary : hashmap """

# \n (new line character) for line breaks

# len() : gets string length
# counts per character including whitespaces ( ), line breaks [\n], and other escape sequences [\"]
print(len(another_pun))

# split([delimiter]) : splits string by set delimeter
"Sun,Mon,Tue,Wed,Thu,Fri,Sat".split(",") # ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

# strip() : removes whitespaces at the start and end of a string
a_long_line = "       This is a long line with some space before, after,     and some space in the middle..    "
a_long_line_stripped = a_long_line.strip()
a_long_line_stripped # 'This is a long line with some space before, after,     and some space in the middle..'

the_3_musketeers = ["Athos", "Porthos", "Aramis"]
str(the_3_musketeers)
# "['Athos', 'Porthos', 'Aramis']"
# FIXME: why did it not use single quotes for list enclosure and double quotes for the elements