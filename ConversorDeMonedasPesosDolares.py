def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cantidad de pesos " + tipo_pesos + ": ")
    pesos = float(pesos) 
    dolares = pesos / valor_dolar
    dolares = round(dolares, 3)
    dolares = str(dolares)
    print("Tienes una cantiad de $" + dolares + " dolares")

menu = input("""Bienevenido al conversor de texto
(1)Colombia
(2)Argentina
(3)Mexico
Elija la opcion de su pais: """)

if menu == "1":
    conversor("colombianos", 3569 )
elif menu == "2":
    conversor("argentinos", 87,30)
elif menu == "3":
    conversor("mexicanos", 20,59)
else:
    print("Ingrese una opcion correcta")







