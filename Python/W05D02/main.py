# import package

# print(package.mod3.ibm('I NEED QUANTUM COMPUTER QUICKLY'))
# print(mod3.ibm('I NEED QUANTUM COMPUTER QUICKLY'))

# print(dir())

# from package import *
# print(dir())

# import package.mod3

# print(mod3.ibm('Give me a QUANTUM PC I just want to play pubg'))

# from package import mod3

# print(mod3.ibm('Give me a QUANTUM PC I just want to play pubg'))

# Package Initialisation.(init file)
# 1) It's not necessary to have an Initialisation file.
# 2) Once Package Initialisation is done, we get the following benefits:
#   2.1) Now if we import package, you can import all the modules which
# 	   are present inside that package.
#   2.2) It can initialise some pre requisite code.

## Special Var __all__ = ['mod3'] (Contains names of the modules which should be impoted with *)
# from package import * (Similar thing in module imports everything)
# from mod1 import * (it imports everything inside mod1)

# BUT IN PACKAGE THE GAME IS DIFFERENT.

# WHEN YOU USE FROM PACKAGE import * , IT imports all the modules which
# are listed inside the __all__ list.
# import * + __all__ MAKES MAGIC.
from package import *
print(dir())
print(mod3.ibm('Give me a QUANTUM PC I just want to play pubg'))

print(mod4.tesla(' i want my supercar delivered in Jaipur quickly!!'))