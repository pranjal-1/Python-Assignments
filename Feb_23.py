##var = 10/10
##print(var)

#Exception --- ZerDivisionError, TypeError,

##try:
##    var = 10/0
##    print(var)
##except:
##    print("sorry")
##print("welcome")

##try:
##    var = "a" + 20
##    print(var)
##except: #default
##    print("sorry")
##print("welcome")

##try:
##    var = 10/0
##    print(var)
##except TypeError: #default
##    print("sorry")
##print("welcome")

##try:
##    var = 10/0
##    print(var)
##except TypeError: #default
##    print("sorry")
##except:
##    print("oops")
##print("welcome")

##try:
##    var = 10/0
##    print(var)
##except TypeError as ex: #default
##    print("sorry")
##except ZeroDivisionError as ex: #default
##    print("ex")
##except:
##    print("oops")
##print("welcome")

##try:
##    var = 10/0
##    print(var)
##except (TypeError,ZeroDivisionError) as ex: #default
##    print("sorry")
##except:
##    print("oops")
##print("welcome")

##try:
##    var = 10/4
##    print(var)
##except (TypeError,ZeroDivisionError) as ex: #default
##    print(ex)
##except:
##    print("oops")
##else:
##    print("welcome")

##try:
##    var = 10/0
##    print(var)
##except (TypeError,ZeroDivisionError) as ex: #default
##    print(ex)
##except:
##    print("oops")
##else:
##    print("welcome")
##finally:
##    print("hhhhhhhhhh")

##try:
##    var = 10
##    if var>5:
##        raise IndexError
##except IndexError:
##    print("jsdhgytds")

##try:
##    var = 10
##    if var>5:
##        raise IndexError
##except IndexError as ex:
##    print(ex)
#empty error

##try:
##    var = 10
##    if var>5:
##        raise IndexError("india india")
##except IndexError as ex:
##    print(ex)

##try:
##    var = 10
##    if var>5:
##        raise MyError("india india")
##except MyError as ex:
##    print(ex)
#error

##class MyError(Exception):
##    pass
##
##try:
##    var = 10
##    if var>5:
##        raise MyError("india india")
##except MyError as ex:
##    print(ex)

##class MyError(Exception):
##    var = "my own error"
##
##try:
##    var = 10
##    if var>5:
##        raise MyError("india india")
##except MyError as ex:
##    print(ex.var)

##class MyError(Exception):
##    var = "my own error"
##
##try:
##    var = 10
##    if var>5:
##        raise MyError("india india")
##except MyError:
##    print(MyError.var)
##





