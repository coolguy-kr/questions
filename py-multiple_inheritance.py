# The following code is an example. The tree structure of class inheritance relationships is displayed as a list on the console.

class X:
    pass

class Y:
    pass

class Z:
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())

# So, It displays a result as a list.

""" Console Output 

[<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>]
"""

# However, I expected a result of below to be printed.
""" The result that I expected

[<class '__main__.M'>, <class '__main__.B'>, <class '__main__.Y'>, <class '__main__.Z'>, <class '__main__.A'>, <class '__main__.X'>, <class 'object'>]
"""

# Q. If we look at them in order, the expected result should be output. Should it?
