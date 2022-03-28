''' P2 -Leer el año de nacimiento de 10 estudiantes del curso de Globant y
calcular cuantos años cumple cada estudiante en 2022, finalmente
indique cuantos estudiantes tienen más de 22 años '''

contador=0

for i in range(1,11):
   
    edad=int(input(f'Ingrese el año de nacimiento del estudiante {i}: '))
    edad2022=2022-edad

    if(edad2022>22 and edad2022>0):
        contador+=1

print(f'La cantidad de estudiantes que tienen más de 22 años son: {contador}')
