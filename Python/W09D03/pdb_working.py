# What is Debugging?
# Options:
# 1) Correcting Error when you already know the
#     error
# 2) Finding the Error
# 3) Step by Step Execution of Code

## Correct Answer: 2) Finding the Error(Logical ones)

## pdb: It is inbuilt python debugger

breakpoint()

a = input()
b = input()

def sum_the_values(a,b):
    print('we are inside the function')
    print(int(a)+int(b))

breakpoint()
sum_the_values(a,b)

## whatis can be used to check the data type of
## variables
## print() can be used to directly print the
## value of that variable.
## c(continue) => continue all the leftover code
## from the current position.
## we can keep the breakpoint anywhere
## n(next) => run the very next piece of code
## s(step inside) => to step inside a funtion such that
## enter will like showing us next line to execute