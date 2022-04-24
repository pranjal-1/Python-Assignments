##class Netzwerk:
##    def __init__(abhi,name):
##        abhi.name = name
##    def fun(abhi):
##        print(abhi.name,"one")
##    def fun(abhi):
##        print(abhi.name,"two")
##n_obj = Netzwerk("kohli")
##n_obj.fun()
##
##
##var = "a"
##var = "b"
##print(var)
##
##python dont support function overloading
##python has access specifier, public private
##private access specifier can also be called as "Data Hiding"

##class Netzwerk:
##    def __init__(abhi,name):
##        abhi.name = name
##
##    def fun(abhi):
##        print(abhi.name,"one")
##
##    def __new(abhi): #private access specifier which can also be called as "data hiding"
##        print(pranjal.name,"two")
##
##n_obj = Netzwerk("kohli")
##n_obj.fun()
##n_obj.new()
##
##

##class Netzwerk:
##    def __init__(self,name,age):
##        self.name = name
##        self.age = age
##
##    def fun(self):
##        print(self.name,"one",self.age)
##
##class Two(Netzwerk):  #single inheritance
##   
##    def new(pranjal):
##        print(pranjal.name,"two")
##
##n_obj = Two("kohli",33)
##n_obj.fun()
##n_obj.new()
##

##class Netzwerk:
##    def __init__(self,name,age):
##        self.name = name
##        self.age = age
##
##    def fun(self):
##        print(self.name,"one",self.age)
##
##class Two(Netzwerk):
##    def __init__(pranjal, name):
##        pranjal.name = name
##        Netzwerk.__init__(pranjal,pranjal.name,33)
##
##    def new(pranjal):
##        print(pranjal.name,"two")
##
##n_obj = Two("kohli")
##n_obj.fun()
##n_obj.new()

##class Netzwerk:
##    def __init__(self,name,age):
##        self.name = name
##        self.age = age
##
##    def fun(self):
##        print(self.name,"one",self.age)
##
##class Two(Netzwerk):
##    def __init__(pranjal, name):
##        pranjal.name = name
##        super().__init__(pranjal.name,33)
##
##    def new(pranjal):
##        print(pranjal.name,"two")
##
##n_obj = Two("kohli")
##n_obj.fun()
##n_obj.new()
