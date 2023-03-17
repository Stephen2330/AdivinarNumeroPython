#Adivinar número entre 0 y 99
#region#Funciones

#Valida si el número del intento es más pequeño
def validaPeq():
    print("El número ", str(intento), " es más pequeño, debe adivinar un número más alto \n")

#Valida si el número del intento es más grande
def validaGrand():
    print("El número ", str(intento), " es más grande, debe adivinar un número más bajo \n")

#Valida si acierta el número
def validaCorrecto():
    print("Se acertó. El número es: ", str(num))
#endregion

#region Código
import random as R # se importa random con alias R
num = R.randint(0, 100) #se asigna un valor aleatorio entre 0 y 99 a variable num

while True: #Ciclo infinito para jugar varias veces
    while True: #Ciclo que permite adivinar varias veces hasta acertar
        intento = int(input("Adivine escogiendo un número entre 0 y 99 incluidos:"))

        try:
            intento = int(intento)
        except:
            pass
        else:
        #Se compara si el número es entre 0 y 99
            if intento >= 0 and intento <= 99:
                break #Sale del ciclo

#Comprobación de si es correcto
    if intento < num:
        validaPeq()
    elif intento > num:
        validaGrand()
    else:
        validaCorrecto()
        break#Se gana y se sale del ciclo
#endregion