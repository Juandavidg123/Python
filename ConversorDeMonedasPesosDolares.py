print("""Bienvenido al conversor
(1)Colombia
(2)Argentina
(3)Mexico
Elija la opcion de su pais: """)

pesos = input("Cantidad de pesos colombianos: ")
pesos = float(pesos)
valor_dolar = 3560 
dolares = pesos / valor_dolar
dolares = round(dolares, 3)
dolares = str(dolares)
print("Tienes una cantiad de $" + dolares + " dolares")