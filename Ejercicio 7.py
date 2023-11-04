Abecedario =  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "W", "x", "y", "z"]
a_1 = []
for x in range (len(Abecedario)):
    if x %3 != 2:
        a_1 += Abecedario[x]
print (a_1)