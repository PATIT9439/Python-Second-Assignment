# from collections import OrderedDict


# a = int(input("Enter first number"))
# b = int(input("Enter second number"))
# c = int(input("Enter third number"))
# d = int(input("Enter fourth number"))
# e = int(input("Enter fifth number"))


# num =[ a, b, c, d, e ]

# if num % 2=0:
   

from collections import OrderedDict
  
od = OrderedDict()
od['a'] = input("input1\n")
od['b'] = input("input2\n")
od['c'] = input("input3\n")
od['d'] = input("input4\n")
od['e'] = input("input5\n")
 

if od.values() % 2==0:
    print(od.values() + "0")
else:
    print(od.values()+"1")

