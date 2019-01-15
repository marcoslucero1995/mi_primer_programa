
print("Adivina un numero")

numero_a_adivinar =input("Ingrese numero ha adivinar: ")

tiempo = 50

print("El juego empieza en...")

while tiempo > 0:
    tiempo -= 1
    print(tiempo)

numero_pensado = input("Ingrese numero pensado: ")

while numero_pensado != numero_a_adivinar:
    numero_pensado = input("Ingrese numero pensado: ")

if numero_a_adivinar == numero_a_adivinar:
        print("Has acertado felicitaciones")










