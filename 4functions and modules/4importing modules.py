#importing module


# to use the function of the module we need to follow the syntax: module_name.function()
import module_name
# eg: 
import math
print(math.sqrt(3)) # square root function

# import everything from module
# while calling the function we dont need to write math.sqrt() only sqrt() works
from module_name import *
# eg:
from math import *

# importing certain function from module
# while calling the function we dont need to write math.sqrt() only sqrt() works
from module_name import function_name #we dont need () with function_name here
# eg:
from math import sqrt

# to see all the functions a module contains use
import math
print(dir(math))

