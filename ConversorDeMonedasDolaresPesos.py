def conversor(valor_dolar):
    pesos = input("Cantidad de dolar: ")
    pesos = float(pesos) 
    dolares = pesos * valor_dolar
    dolares = round(dolares, 3)
    dolares = str(dolares)
    print("Tienes una cantiad de $" + dolares + " pesos")
    print("nota: se han tomado el valor del dolar de la fecha 29/01/2021")

menu = input("""Bienevenido al conversor de monedas
(1)Colombia
(2)Argentina
(3)Mexico
Elija la opcion de su pais: """)

if menu == "1":
    conversor(3569)
elif menu == "2":
    conversor(87.30)
elif menu == "3":
    conversor(20.59)
else:
    print("Ingrese una opcion correcta")
