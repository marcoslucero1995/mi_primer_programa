

operacion_a_realizar = str(input("¿Que operacion deseas realizar? (suma / resta / division / multiplicacion: ")).upper()

primer_numero = int(input("Ingresa primer numero: "))

segundo_numero = int(input("Ingresa segundo numero: "))

resultado = 0


if operacion_a_realizar == "SUMA":
    resultado = primer_numero + segundo_numero
    print("El resultado de la operacion es {}".format(resultado))

elif operacion_a_realizar == "RESTA":
    resultado = primer_numero - segundo_numero
    print("El resultado de la operacion es {}".format(resultado))

elif operacion_a_realizar == "DIVISION":
    resultado = primer_numero / segundo_numero
    print("El resultado de la operacion es {}".format(resultado))

elif operacion_a_realizar == "MULTIPLICACION":
    resultado = primer_numero * segundo_numero
    print("El resultado de la operacion es {}".format(resultado))
