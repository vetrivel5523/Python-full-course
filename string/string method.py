#upper()- capital
#lower()- small
#replace()- change items
#strip()- correct allignment
#count()- count how many "s" in string
#upper()
a="kongunadu vetrivel ece"
print(a.upper())
#lower()
a="kongunadu vetrivel ece"
print(a.lower())
#replace()
a="kongunadu vetrivel ece"
print(a.replace("ece","***"))
#strip()
a="          kongunadu vetrivel ece"
print(a)
print(a.strip())
#count()
a="kongunadu vetrivel ece"
print(a.count("e"))
#add 2 sring
a="vetri"
b="vel"
c=a+b
print(c)
#
a="vetri"
b="vel"
print(a,b)

#another add
a="vetri"
b="vel"
c=a+""+b
print(c)

#string format

quantity=500
price=10000
item="apple"
txt="the {} i need {} but cost {} is high"
print(txt.format(item,quantity,price))