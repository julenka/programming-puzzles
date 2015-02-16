__author__ = 'julenka'

def toNum(c):
    return  ord(c) - 96

def ans(s):
    return sum((toNum(c) for c in s))

a = "honeycomb"
b = "homesteaders"
c = "evernote"
d = "mjolnir"

for x in [a,b,c,d]:
    print x, ans(x)
