def is40(numA, numB):  # Verifica si la suma de dos numeros es 40
    addition = numA + numB  # Suma los numeros ingresados
    if(addition == 40):
        return True
    else:
        return False


firstNum = 20
secondNum = 20
if(is40(firstNum, secondNum)):  # Suma 20 y 20, obteniendo 40 e
    # imprimiendo el mensaje correspondiente
    print("¡Es 40!")
else:
    print("No es 40")
