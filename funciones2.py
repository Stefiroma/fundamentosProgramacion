def retornar_mayor(v1,v2):
    if v1>v2:
        mayor=v1
    else:
        mayor=v2
    while(v1==v2):
        print('El número es igual.')
    return mayor

    

#bloque pricipal
valor1=int(input("Ingrese el primer valor:"))
valor2=int(input("Ingrese el segundo valor"))
print(retornar_mayor(valor1,valor2))
