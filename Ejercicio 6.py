list1 = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
suspensos = []
Aprobadas =[]
for x in list1:
    nota = float (input (f"¿Cuanto sacaste en {x}?"))
    notas.append (nota)
    if nota < 5:
        suspensos.append (x)
        if nota >= 5:
            Aprobadas.append (x)
            list1.remove (Aprobadas)  
if suspensos:
    print ("Tienes que repetir", suspensos)