#Adivinar el número
import random
random_number=random.randint(0,50)
guess_num = int(input("Ingresá un número: "))
while guess_num != random_number:
    if guess_num < random_number:
        guess_num = int(input("El número a adivinar es mayor. Ingresá otro número: "))
    else:
        guess_num = int(input("El número a adivinar es menor. Ingresá otro número: "))
print("Adivinaste, el número es: ",guess_num)
