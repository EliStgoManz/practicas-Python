#Almacenamos el numero más grande actual aquí
numeroMayor= -999999999

#ingresa el primer valor
numero = int(input("introduczca un número o escriba -1 para detener: "))


#si el numero no es igual a -1,continuaremos
while numero!=-1:
    #¿Es el número más grande que el número más grande?
    if numero>numeroMayor:
        #si si, actualiza el mayor número
        numeroMayor=numero
        #ingresa el siguiente número
        numero=int(input("introduce un número o escribe -1 para detener:"))

#imprimir el número más grande
print("El número más grande es: ",numeroMayor)
        
