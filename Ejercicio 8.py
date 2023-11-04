p_i = input ("Palabra:")
p_i.lower ()
if p_i == p_i [::-1]:
    print ("¡La palabra", p_i, "es un palindromo!")
else:
    print ("¡La palabra", p_i, "no es un palindromo!")