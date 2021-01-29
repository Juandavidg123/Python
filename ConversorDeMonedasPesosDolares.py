menu = input("""Bienevenido al conversor de texto
(1)
(2)
(3)
Elija la opcion de su pais: """)


    pesos = input("Cantidad de pesos colombianos: ")
    pesos = float(pesos)
    valor_dolar = 3560 
    dolares = pesos / valor_dolar
    dolares = round(dolares, 3)
    dolares = str(dolares)
    print("Tienes una cantiad de $" + dolares + " dolares")


