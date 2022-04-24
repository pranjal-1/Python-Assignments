# var = ["a","b","c"]
# for x in var:
#     var.append(x.upper())
#
# print(var)
# output : no output

# var = "abc"
# for x in var:
#     var = var + x.upper()
#
# print(var)

var = ["a","b","c","d","e","f"]
x,y in enumerate(var):
    if x%2 == 0:
        var = var + y
print(var)