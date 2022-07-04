class A:
    num = 10
class B(A):
    pass
class C(A):
    num = 1
class D(B,C):
    pass

print(D.__mro__) #SEE THE PATH PYTHON IS TAKING THROUGH THE OBJECTS