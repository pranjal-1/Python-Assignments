# var = []
# print(type(var))
#output : <class 'list'>

# var = ["dhoni",55,44.5,"ab",["a","b"]]
# print(type(var))
# print(var[3])
# output : <class 'list'>
# ab

# var = ["a","b","c"]
# var[1] = "d"
# print(var)
# output : ['a', 'd', 'c']

# var = ["a","b","c"]
# print(dir(var))
# output : ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# var = ["a","B"]
# var1 = ["c","d"]
# print(var + var1)
# output : ['a', 'B', 'c', 'd']

# a = ["dhoni","kohli","ashwin"]
# b = a  #shallow copy
# print(a)
# print(b)
# b[0] = "rohit"
# print(a)
# print(b)
# output :
# ['dhoni', 'kohli', 'ashwin']
# ['dhoni', 'kohli', 'ashwin']
# ['rohit', 'kohli', 'ashwin']
# ['rohit', 'kohli', 'ashwin']

# a = ["dhoni","kohli","ashwin"]
# b = a[:]  #deep copy
# print(a)
# print(b)
# b[0] = "rohit"
# print(a)
# print(b)
# output:
# ['dhoni', 'kohli', 'ashwin']
# ['dhoni', 'kohli', 'ashwin']
# ['dhoni', 'kohli', 'ashwin']
# ['rohit', 'kohli', 'ashwin']

# var = ["a", "b", "c"]
# var.insert(0,"dhoni")
# print(var)
# output : ['dhoni', 'a', 'b', 'c']

# var = ["a", "b", "c"]
# var.append("dhoni")
# print(var)
# output : ['a', 'b', 'c', 'dhoni']

# var = ["a", "b", "c"]
# var.append("dhoni","kohli")
# print(var)
#output : error

# var = ["a", "b", "c"]
# var.extend(["dhoni","kohli"])
# print(var)
# output : ['a', 'b', 'c', 'dhoni', 'kohli']

# var = ["a", "b", "c"]
# var.append(["dhoni","kohli"])
# print(var)
# output : ['a', 'b', 'c', ['dhoni', 'kohli']]

# var = ["a", "b", "c"]
# var.insert(10,"dhoni")
# print(var)
# output: ['a', 'b', 'c', 'dhoni']


# var = ["a", "b", "c"]
# print(var.extend(("dhoni","kohli")))
#
# var = ["a", "b", "c"]
# output = var.extend(("dhoni","kohli"))
# print(output)
# output : None
#
# var = ["dhoni","and","cat",4,3,2,5,3,"apple","goat"]
# var.sort()
# print(var)
# output : error

# var = ["dhoni","and","cat","apple","goat"]
# var.sort()
# print(var)
# output : ['and', 'apple', 'cat', 'dhoni', 'goat']

# var = ["dhoni","and","cat","apple","goat"]
# var.sort(reverse = True)
# print(var)
# output : ['goat', 'dhoni', 'cat', 'apple', 'and']

# var = ["dhoni","and","cat","apple","goat"]
# output = sorted(var,reverse = True)
# print(var)
# output : ['dhoni', 'and', 'cat', 'apple', 'goat']

# var = ["dhoni","and","cat","apple","goat"]
# output = sorted(var,key = len)
# print(var)
# output : ['dhoni', 'and', 'cat', 'apple', 'goat']

# var = ["dhoni","and","cat","apple","goat"]
# var.sort(key = len)
# print(var)
# output : ['and', 'cat', 'goat', 'dhoni', 'apple']

# var = ["dhoni","and","cat","apple","goat"]
# var.pop()
# print(var)
# output: ['dhoni', 'and', 'cat', 'apple']

# var = ["dhoni","and","cat","apple","goat"]
# var.pop(2)
# print(var)
# output : ['dhoni', 'and', 'apple', 'goat']

# var = ["dhoni","and","cat","apple","goat"]
# var.remove("apple")
# print(var)
# output : ['dhoni', 'and', 'cat', 'goat']

# var = ["dhoni","and","cat","apple","goat"]
# var.clear()
# print(var)
# output : []

# var = ["dhoni","and","cat","apple","goat"]
# del var
# print(var)
# output : error

# var = ["dhoni","and","cat","apple","goat"]
# del var[4]
# print(var)
# output : ['dhoni', 'and', 'cat', 'apple']

# var = ["dhoni","and","cat","apple","goat"]
# del var[14]
# print(var)
# output: IndexError: list assignment index out of range

# var = ("dhoni","kohli")
# print(type(var))
# #output : <class 'tuple'>
#
# var = ("a","b")
# var[0] = "dhoni"
# print(var)
# output : error
# <class 'tuple'>

# var = ("a","b")
# print(dir(var))
# output : ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']


# var = ("dhoni",)
# print(type(var))
# output : <class 'tuple'>