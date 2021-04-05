# import mod1
# output = mod1.spacex('land us on mars')
# print(output)
# output2 = mod1.google('make an amazing search engine')
# print(output2)
# print(mod1.pi)

# import mod2

# output = mod2.Microsoft('Please dont update windows in middle of some work')

# output2 = mod2.Netflix('I dont want to watch Bandersnatch!!')

# print(output)
# print(output2)

# We can import the modules if they are present in :
# 1) Same Directory
# 2) Python sys path

# import math
# print(math.pi)

# import sys

# print('We can import modules from these paths')
# for i in sys.path:
# 	print(i)

# dir() -> All the names in that namespace

# import math
# print(dir(math))
# print(math.log10(100))

# import mod1
# print(dir(mod1))
# print(mod1.__file__)

## aliasing

# import math as m

# print(m.pi)
# print(m.cos(0))

from mod1 import * # import everything which is present in mod1 and we can use it directly like if it is defined in the same file.

output = spacex('LAND US ON JUPYTER')
output2 = google('MAKE AN AMAZING AI')

# print(output)
# print(output2)

# print(pi)

# globals() and locals()
# print('**globals',globals())
# print('**LOCALS',locals())