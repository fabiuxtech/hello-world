# some exercises
#x = input("Come ti chiami? ")
#y = input("quanti anni hai? ")
#print("La variabile x contiene: " + x + "\nLa variabile y contiene: " + y)
#print("Mi chiamo " + x + " e ho " + y + " anni")
#print("x è di tipo:", type(x))
#print("y è di tipo:", type(y))
#if int(y) >= 18: 
#    print("Sei maggiorenne!")
#else: 
#    print("Non sei maggiorenne")
##################################
my_food_list=[]
my_food_list.append(input("Cosa vuoi comprare? "))
print("Lista della spesa: ",my_food_list)
addq=input("Vuoi aggiungere altro? S/N\n")
if addq.lower() == "n":
    print("Ok, ciao\n")
    exit
elif addq.lower() == "s":
    my_food_list.append(input("Cos'altro vuoi aggiungere? "))
    print("Lista della spesa aggiornata: ", my_food_list)
else:
    print("risposta non riconosciuta")
    exit