p = input ("palabra:")
p.lower ()
vocales = ["a", "e", "i", "o", "u"]
a = 0
e = 0
i = 0
o = 0
u = 0
for a in range (len(p)):
    if p [a] == vocales [0]:
        a += 1
print (a)