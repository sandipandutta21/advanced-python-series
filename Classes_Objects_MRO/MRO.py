class A:
    def func(self):
        print("B.func() called")

class B(A):
    def func(self):
        print("B.func() called")

class C(B, A):
    pass

c = C()
c.func()

"""
    Output of the above code:
    C -> B -> A -> object
"""

class A:
    def func(self):
        print("A.func() called")

class B:
    def func(self):
        print("B.func() called")

class C(A, B):
    pass

class D(C, B):
    pass

d = D()
d.func()

"""
    Output of the above code:
    D -> C -> A -> B -> object.
"""