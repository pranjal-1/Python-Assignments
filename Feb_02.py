#var = "dhoni"
#print(var[0])

#d - 0
#h - 1
#o - 2
#n - 3
#i - 4

#var[4] = "y"

#python string slicing

#var = "dhoni msd"
#print(var[0])
#print(var[0:])
#print(var[0:6])
#print(var[6:2])
#print(var[-1])
#print(var[-1:])
#print(var[-2:])
#print(var[::2])
#print(var[::-2])
#print(var[::-1]) #string reversal




#var = "dhoni"
#var1 = "msd"
#print(var + var1)
#output : dhonimsd




#var = "dhoni"
#var1 = 90
#print(var + var1)
#output : TypeError: can only concatenate str (not "int") to str



#var = "dhoni"
#var1 = 90
#print(var + str(var1))
#output : dhoni90



#var = "dhoni","msd"
#print(var)
#print(type(var))
#output : ('dhoni', 'msd')
           #<class 'tuple'>



#var, var1 = "dhoni","msd"
#print(var)
#print(var1)
# #output : dhoni
            #msd



#name = "dhoni"
#score = 183
#statement = "captain " + name + " scored " + str(score) + " against srilanka"
#statement = "captain %s scored %d against srilanka"%(name,score)
#statement = "captain {} scored {} against srilanka".format(name,score)
#statement = f"captain {name} scored {score} against srilanka"
#print(statement)   #output : captain dhoni scored 183 against srilanka

#var = "dhoni is my captain and
#he plays for csk"
#print(var)
#output :
  #var = "dhoni is my captain and
   #       ^
#SyntaxError: unterminated string literal (detected at line 75)


#var = """dhoni is my captain and
#he plays for csk"""
#print(var)
#output :
#dhoni is my captain and
#he plays for csk



#var = """dhoni is my captain and \
#he plays for csk"""
#print(var)
#output : dhoni is my captain and he plays for csk



#var = "dhoni is my captain and \
#he plays for csk"
#print(var)
#output : dhoni is my captain and he plays for csk



#path = "c:\newfolder\test.txt"
#print(path)
#output :
#c:
#ewfolder	est.txt



#path = r"c:\newfolder\test.txt"  #rawdata
#print(path)
#output : c:\newfolder\test.txt



#var = input("enter your name: ")
#print(var)
#output : enter your name: pranjal
#pranjal


#var = input()
#print(var)

#var = input("enter your name: ")
#print(var)
#print(type(var))
#output:
#enter your name: pranjal
#pranjal
#<class 'str'>

#var = input("enter your name: ")
#print(var)
#print(type(var))
#output : enter your name: 90
#90
#<class 'str'>


var = int(input("enter your name: "))
print(var)
print(type(var))
#output : enter your name: 90
#90
#<class 'int'>

