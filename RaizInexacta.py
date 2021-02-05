numero = int(input('Escribe un numero: '))
numero_defecto = 0.001
operacion = numero_defecto ** 2
resultado = 0.0 

while abs(resultado ** 2 - numero) >= numero_defecto and resultado <=numero:
    resultado = resultado + operacion

if abs(resultado ** 2 - numero)>= numero_defecto:
    print(f'no se encontro la raiz cuadrada de {numero}')
else:
    print(f'la raiz cuadrada de {numero} es {resultado}')
