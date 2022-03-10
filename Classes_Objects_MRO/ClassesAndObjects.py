class A:
    def __init__(self, var=0):
        self.var = var
   
    def __str__(self):
        return "This is class A"
a = A()
print(a)

"""
    All classes are inherited from object class. 
    > class MyClass:
    >      pass
    >
    > print(MyClass.__class__.__bases__)
    (<class 'object'>,)
"""


class B:

    def __new__(cls, *args, **kwargs):
        """ 
            This will be executing first. 
            It is used to create the object.
        """
        print("__new__ running", cls, args, kwargs)
        return super(B, cls).__new__(cls)

    def __init__(self, *args, **kwargs):
        """
            __init__() uses the same object that __new__() returns
            and initialize it.
        """
        print("__init__ running", self, args, kwargs)
        return super(B, self).__init__(*args, **kwargs)


class MyMetaClass(type):
    """ Ignore this class for now """
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print(f'Meta.__prepare__(mcs={mcs}, name={name}, bases={bases}, {kwargs})')
        return {}


class C(metaclass=MyMetaClass):
    """ Ignore 'metaclass=' part for now """
    var1 = 'variable 1'
    var2 = 'variable 2'

"""
    When an object of class is created, the following happens due to __prepare__().
    obj['var1'] = 'variable 1'
    obj['var2'] = 'variable 2'
"""


class SingletonPattern:     
    """ Use case of modifying the __new__() method """
    def __new__(cls, *args, **kwargs):   
     
        if cls._instance is None: # Checking if an instance of this class exists            
            cls._instance = super().__new__(cls, *args, **kwargs) # Creating a new instace           
        return cls._instance # Returing the instance 
        