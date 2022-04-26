numeroMayor=-99999999
contador=0

while True:
    numero= int(input("ingresa un numero o escribe -1 para finalizar el programa: "))
    if numero== -1:
        break
    contador=1
    if numero>numeroMayor:
        numeroMayor=numero

if contador!=0:
    print("El número más grande es",numeroMayor)
else:
    print("no ha ingresado ningún número")
