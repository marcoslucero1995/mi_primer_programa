
primer_numero = 0
segundo_numero = 0

operacion_a_realizar =  input("¿Que operacion deseas realizar? ( + : - : / : *: ")

operacion_a_realizar == "+" or "-" or "/" or "*"

primer_numero = float(input("Ingresa primer numero: "))

segundo_numero = float(input("Ingresa segundo numero: "))

primer_numero == float

suma = primer_numero + segundo_numero

resta = primer_numero - segundo_numero

multiplicacion = primer_numero * segundo_numero

division = primer_numero / segundo_numero

resultado = 0

if operacion_a_realizar == "+":
    resultado = suma
    print("El resultado de la operacion es {}".format(resultado))

elif operacion_a_realizar == "-":
    resultado = resta
    print("El resultado de la operacion es {}".format(resultado))

elif operacion_a_realizar == "/":
    resultado = division
    print("El resultado de la operacion es {}".format(resultado))

elif operacion_a_realizar == "*":
    resultado = multiplicacion
    print("El resultado de la operacion es {}".format(resultado))

