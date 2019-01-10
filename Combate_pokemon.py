
pokemon_a_elegir = input("¿Contra que pokemon quieres combatir? Charmander / Bulbasaur / Squirtle: ").upper()

vida_pikachu = 100
vida_enemigo = 0
ataque_pokemon = 0

if pokemon_a_elegir == "CHARMANDER":
    vida_enemigo = 80
    nombre_pokemon = "Charmander"
    ataque_pokemon = 7

elif pokemon_a_elegir == "BULBASAUR":
    vida_enemigo = 100
    nombre_pokemon = "Bulbasaur"
    ataque_pokemon = 10

elif pokemon_a_elegir == "SQUIRTLE":
    vida_enemigo = 90
    nombre_pokemon = "Squirtle"
    ataque_pokemon = 8

while vida_pikachu > 0 and vida_enemigo > 0:

    ataque_elegido = input("¿Que ataque vamos a elegir? (Chispazo / Bola voltios)").upper()

    if ataque_elegido == "CHISPAZO":
        vida_enemigo -= 10

    elif ataque_elegido == "BOLA VOLTIOS":
        vida_enemigo -= 12

    print("La vida de {} ahora es de {}".format(nombre_pokemon, vida_enemigo))

    print("{} te ha echo ataque que causa {} de daño".format(nombre_pokemon, ataque_pokemon))

    vida_pikachu -= ataque_pokemon

    print("La vida de pikachu es {}".format(vida_pikachu))

if vida_enemigo <= 0:
    print("Ha ganado pikachu")
else:
    print("Has perdido")
print("el combate ha terminado")
