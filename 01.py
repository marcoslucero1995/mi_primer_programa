apetece_un_helado_input = input("¿Te apetece un helado?) (Si o No): ").upper()

if apetece_un_helado_input == "SI":
    apetece_un_helado = True
elif apetece_un_helado_input == "NO":
    apetece_un_helado = False
else:
    print("Te dije que pusieras si o no, no se que has puesto pero lo tomo como no")
    apetece_un_helado = False


tienes_dinero_input = input("¿Tienes dinero para pagarlo? (Si o No): ").upper()
esta_el_señor_de_los_helados_input = input("¿Esta el señor de los helados? (Si o No): ").upper()
esta_tu_tia_input = input("¿Estas con tu tia? (Si o No): ").upper()

apetece_un_helado = apetece_un_helado_input == "SI"
puedes_permitirtelo = tienes_dinero_input == "SI" or esta_tu_tia_input == "SI"
esta_el_señor_de_los_helados = esta_el_señor_de_los_helados_input == "SI"



if  apetece_un_helado and puedes_permitirtelo and esta_el_señor_de_los_helados:
    print("Tomate un helado")

else:
    print("pues nada")