#!/usr/bin/env python3
# Student ID: pranjo
def function1():
    # This object 'a' is completely unrelated to the object 'a' in function2():
    a = 'object_function1'
    print('print() call in function1 on a:',a)

def function2():
    # This variable 'a' is completely unrelated to the variable 'a' in function1():
    a = 'function2_object'
    print('print() call in function2 on a:',a)

# Note that you cannot access the value of object '''a''' created in function1()
# or function2() with the print() functions after the calling function1() and function2()
# All the print() retrieved the value of object '''a''' defined in the main script.
a = 'object_in_main'
print('print() call in main on a:',a)
function1()
print('print() call in main on a:',a)
function2()
print('print() call in main on a:',a)