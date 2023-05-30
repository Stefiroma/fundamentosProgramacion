suma= 0
x=1
canNum = int(input("Digite Cantidad de Numeros: "))
for x in range(canNum):
    print("Digite un numero : ",x+1," : ")
    num=int(input())
    suma = suma+num
 # Fin del bloque de instrucciones que se repiten 
print ("la suma es : ", suma)
