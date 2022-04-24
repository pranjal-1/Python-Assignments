##class is template
##class is going to have everything needed for the program to execute
##class in general is called a collection of objects
##Vehicle --
##class is to form a structure

##var = "dhoni"
##def fun():
##    print("welcome")
##
##print(var)
##fun()


##class Netzwerk:
##    
##    var = "dhoni"
##    def fun():
##        print("welcome")
##
##print(Netzwerk.var)
##Netzwerk.fun()

##class Netzwerk:
##    
##    var = "dhoni"
##    def fun():
##        print("welcome")
##        
##n_obj = Netzwerk  external object reference---lot of memory
##print(n_obj.var)
##n_obj.fun()

##class Netzwerk:
##    
##    def fun(self,name):
##        print(name)
##
##    def new(self,name):
##        print(name)
##        
##n_obj = Netzwerk()    #constructor -- requires less memory
##n_obj.fun("dhoni")
##n_obj.new("dhoni")

class Netzwerk:

    def __init__(self,name):

        self.name = name
    
    def fun(self,name):
        print(self.name)

    def new(self,name):
        print(self.name)
        
n_obj = Netzwerk("kohli")    #constructor -- requires less memory
n_obj.fun()
##n_obj.new()

