# some exercises
x = input("Come ti chiami? ")
y = input("quanti anni hai? ")
print("La variabile x contiene: " + x + "\nLa variabile y contiene: " + y)
print("Mi chiamo " + x + " e ho " + y + " anni")
print("x è di tipo:", type(x))
print("y è di tipo:", type(y))
if int(y) >= 18: 
    print("Sei maggiorenne!")
else: 
    print("Non sei maggiorenne")