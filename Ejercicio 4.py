n_ganadores= []
for i in range (8):
    ganadores = int (input ("Numero ganador:"))
    n_ganadores.append (ganadores)
n_ganadores.sort ()
print (n_ganadores)