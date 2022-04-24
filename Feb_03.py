# var = "dhoni"
# for x in var:
#     print(x)
# output :
# d
# h
# o
# n
# i




# var = "dhoni"
# for x in var:
#     print(x, end = "")
# output : dhoni





# var = "dhoni"
# for x in var:
#     print(x, end = "_")
#output : d_h_o_n_i_





# var = "dhoni"
# for x in enumerate(var):
#     print(x)
# output:
# (0, 'd')
# (1, 'h')
# (2, 'o')
# (3, 'n')
# (4, 'i')





# var = "dhoni"
# for x,y in enumerate(var):
#     print(x)
#     print(y)
# output :
# 0
# d
# 1
# h
# 2
# o
# 3
# n
# 4
# i



# var = "dhoni"
# print(len(var))
# output : 5

# var = "dhoni"
# my_counter = 0
# for x in var:
#     my_counter = my_counter + 1
# print(my_counter)
# output : 5

# var = "dhoni is my captain"
# for x in var:
#     if x == "i":
#         print("success")
# output :
# success
# success
# success

# var = "dhoni is my captain"
# for x in var:
#     if x == "i":
#         print("success")
#     else:
#         print("failure")
# output:
# failure
# failure
# failure
# failure
# success
# failure
# success
# failure
# failure
# failure
# failure
# failure
# failure
# failure
# failure
# failure
# failure
# success
# failure

# var = "dhoni is my captain"
# for x in var:
#     if x == "i":
#         print(x,"success")
#     else:
#         print(x,"failure")
# output :
# d failure
# h failure
# o failure
# n failure
# i success
#   failure
# i success
# s failure
#   failure
# m failure
# y failure
#   failure
# c failure
# a failure
# p failure
# t failure
# a failure
# i success
# n failure


# var = "dhoni is my captain"
# for x in var:
#     if x == "i":
#         print(x,"success")
#     elif x == "a":
#         print(x,"success")
#     else:
#         print(x,"failure")
# output :
# d failure
# h failure
# o failure
# n failure
# i success
#   failure
# i success
# s failure
#   failure
# m failure
# y failure
#   failure
# c failure
# a success
# p failure
# t failure
# a success
# i success
# n failure


# var = "dhoni is my captain"
# for x in var:
#     if x == "i" or x == "a":
#         print(x,"success")
#     else:
#         print(x,"failure")
# output:
# d failure
# h failure
# o failure
# n failure
# i success
#   failure
# i success
# s failure
#   failure
# m failure
# y failure
#   failure
# c failure
# a success
# p failure
# t failure
# a success
# i success
# n failure


# var = "dhoni is my captain"
# for x in var:
#     if x == "i" or x == "a":
#         print(x,"success")
#         break
#     else:
#         print(x,"failure")
# output :
# d failure
# h failure
# o failure
# n failure
# i success


# var = "dhoni is my captain"
# for x in var:
#     if x == "i":
#         continue
#     print(x,"Success")
# output:
# d Success
# h Success
# o Success
# n Success
#   Success
# s Success
#   Success
# m Success
# y Success
#   Success
# c Success
# a Success
# p Success
# t Success
# a Success
# n Success

# var = "dhoni is my captain"
# for x,y in enumerate(var):
#     if y == "i" or y == "a":
#         print(x,"success")
#         break
#     else:
#         print(x,"failure")

# var = "dhoni is my captain"
# for x,y in enumerate(var):
#     if(x % 2 == 0):
#         print(x,"success")

# var = "dhoni is my captain"
# odd_var = ""
# even_var = ""
# for x,y in enumerate(var):
#     if x % 2 == 0:
#         even_var += y
#     else:
#         odd_var += y
# print("Odd var:", odd_var)
# print("Even var:", even_var)
# output :
#Odd var: hn sm ati
# Even var: doii ycpan
