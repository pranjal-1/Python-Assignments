class My_Class:
    """This is called defined with functions that takes arguments """
    def __init__(self, name, age):  #instant + initializer
##anything that has double underscore on either side is called "attributes" or "magic methods"
##self is called object reference for inside class        
        self.name = name
        self.age = age

    def one(self):
        print(self.name)

    def two(self):
        print(self.age, self.name)

my = My_Class("dhoni",33)
##my is called single object instant reference for outside activity
##My_Class is called constructor
##By default all the constructor will have one hidden argument in the first position
my.one()
my.two()
print(my.__doc__)
