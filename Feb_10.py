##print("hello")
##print("welcome to hdfc")

##def fun():
##
##    print("hello")
##    print("welcome to hdfc")
##
##fun()
##fun()
##fun()

##def fun(var):
##
##    print("hello",var)
##    print("welcome to hdfc")
##
##fun("dhoni")
##fun("kohli")
##fun("ashwin")
##fun(5)

##def fun(var):
##
##    if isinstance(var,str):
##        print("hello",var)
##        print("welcome to hdfc")
##
##fun("dhoni")
##fun("kohli")
##fun("ashwin")
##fun(5)


##def fun(var,country):
##
##    if isinstance(var,str):
##        print("hello",var,"from",country)
##        print("welcome to hdfc")
##
##fun("dhoni","india")
##fun("kohli","australia")
##fun("ashwin",2)

##def fun(var,country):
##
##    if isinstance(var,str) and isinstance(country,str):
##        print("hello",var,"from",country)
##        print("welcome to hdfc")
##
##fun("dhoni","india")
##fun("kohli","australia")
##fun("ashwin",2)

##def fun(var,country):
##
##    if isinstance(var,str) and isinstance(country,str):
##        print("hello",var,"from",country)
##        print("welcome to hdfc")
##
##fun(country = "india",var = "dhoni") #sequence
##fun("kohli","australia")
##fun("ashwin",2)


##def fun(var,country = "india"):
##
##    if isinstance(var,str) and isinstance(country,str):
##        print("hello",var,"from",country)
##        print("welcome to hdfc")
##
##fun("kohli")
##fun("kohli","australia")


##def fun(var = "dhoni",country = "india"):
##
##    if isinstance(var,str) and isinstance(country,str):
##        print("hello",var,"from",country)
##        print("welcome to hdfc")
##fun()
##fun("kohli")
##fun("kohli","australia")

##def fun(var = "dhoni",country):
##
##    if isinstance(var,str) and isinstance(country,str):
##        print("hello",var,"from",country)
##        print("welcome to hdfc")
##fun()
##fun("kohli")
##fun("kohli","australia")
##
##output: error


##def Passed_Students(name):
##    print(name)
##
##Passed_Students("dhoni")

##def Passed_Students(*name):
##    print(name)
##
##Passed_Students("dhoni","kohli")

##def Passed_Students(*var):
##    print(var)
##    print(type(var))
##
##Passed_Students(name="dhoni",Age=44)
##Passed_Students(name="kohli",Team="rcb")
##output: error

##def Passed_Students(**var):
##    print(var)
##    print(type(var))
##
##Passed_Students(name="dhoni",Age=44)
##Passed_Students(name="kohli",Team="rcb")


##def student_marks(name,eng,maths):
##    total = eng + maths
##    return
##print(student_marks("dhoni",44,55))

##def student_marks(name,eng,maths):
##    total = eng + maths
##    return
##    print("welcome")
##print(student_marks("dhoni",44,55))

def student_marks(name,eng,maths):
    total = eng + maths
    return total,name
print(student_marks("dhoni",44,55))

