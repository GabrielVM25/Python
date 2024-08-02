bool 
"Trabajo del curso de Programación, fecha: 31 de Julio del 2024"
print ("Calculos")
a = int(5)
b = int(18)
c = int(21)
d = int(7)
e = float(2.5)
f = float(5.5)
g = float(7.5)
h = complex(a, 12)
i = complex(12, -7)
j = complex(h, 15)
print ("Sumas")
print (a+b)
print (e+f+g)
print (a+c+h+j+j+j+d+e+b+i)
print (i+j+i+h+i+j+i+h+j)
print ("Restas")
print (a-b-c)
print (e-f-g)
print (h-i-j)
print (c-e-i)

print ("Multiplicación")
print (a*b*c)
print (e*f*g)

print ("División")
print (c/a/b)
print (f/g/e)

"EXTRA"
import random
print ("Juego de adivinar el número en Python.")

attempts = 0
print ("Hola, cuál es tu nombre?")
name = input()

number = random.randint(1,30)
print ("Ëstoy pensando en un numero entre 1 y 20, " + name + ", puedes adivinarlo?")

while attempts < 6:
    print("Adivina el número, mucha suerte.")
    estimate = input()
    estimate = int(estimate)

    attempts = attempts + 1

    if estimate > number:
        print ("Más alto de lo que debería, intenta otra vez.")

    if estimate < number:
        print ("Más bajo de o que debería, intenta nuevamente.")

    if estimate == number:
        attempts = str(attempts)
        print ("Lo has conseguido," + name + ", lograste adivinar el número en," + attempts, " intentos!")

if estimate != number:
    number = str(number)
    print ("Has fallado, pensaba en el número" + number)

    

