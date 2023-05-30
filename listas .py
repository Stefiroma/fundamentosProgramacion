nombre = []
edad  = []
for x in range(5):
    nom=input('Digite el nombre de la persona: ')
    nombre.append(nom)
    ed=int(input('Ingrese la edad de dicha persona: '))
    edad.append(ed)
print('Nombre de las personas mayores de edad: ')
for x in range(5):
    if edad[x]>=18:
        print(nombre[x])
        