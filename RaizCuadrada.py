numero = int(input('Escoge un numero: '))
respuesta = 0

while respuesta **2 < numero:
    respuesta = respuesta + 1

if respuesta**2 == numero:
    print(f'La raiz cuadrada exacta es {respuesta}')
else:
    print('No tiene raiz cuadrada exacta')
