#lee tres numeros
numero1= int(input("ingresa el primer número: "))
numero2=int(input("ingresa el segundo número: "))
numero3=int(input("ingresa el tercer número: "))

#asumimos temporalmente que el primer número
#es el mas grande 
#lo verificamos pronto
nmasGrande= numero1

#comprobamos si el segundo número es más grande que el mayor número
#y actualiza el número más grande si es necesario
if numero2>nmasGrande:
     nmasGrande=numero2
     
#Comprobamos si el tercer número es más gran que el mayor número
#y actualiza el número más grande si es necesario
if numero3>nmasGrande:
    nmasGrande=numero3
    
#imprimir el resultado
print("El número más grande es: ",nmasGrande)
