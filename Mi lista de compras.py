
mi_lista = []

input_usuario = ""

while input_usuario != "FIN":
    input_usuario = input("¿Que deseas comprar? (Escribe FIN para salir): ")

    if input_usuario != "FIN":

        mi_lista.append(input_usuario)

for item in mi_lista:
    print("Tengo que comprar{}".format(item))

print("Esta es la lista de compras")


