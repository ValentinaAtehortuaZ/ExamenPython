''' P1-Construir un programa que permita ingresar N (cantidad digitada por el
usuario) números enteros y cuente cuantos múltiplos de 2, de 3 y
cuantos negativos fueron ingresados '''

numero = int(input("Digita la cantidad de números que va a ingresar: "))
i = 0
multiplo2 = 0
multiplo3 = 0
negativos = 0
multiplos = 0

while(i<numero):
   
    i+=1
    num = input("Digite un número: ")

    if(num.isnumeric()==False):
        print("Digite un valor válido ")
        i-=1
    else:
        numeroVerdadero=int(num)    
       
        if(numeroVerdadero%2==0):
            multiplo2 = multiplo2+1

        if(numeroVerdadero%3==0):
            multiplo3 = multiplo3+1

        if(numeroVerdadero%2==0 and numeroVerdadero%3==0):
            multiplos = multiplos+1  

        if(numeroVerdadero<0):
            negativos = negativos+1

print(f"Los multiplos de 2 son: {multiplo2}")
print(f"Los multiplos de 3 son: {multiplo3}")
print(f"Los multiplos de 2 y 3 son: {multiplos}")
print(f"Los números negativos son: {negativos}") 