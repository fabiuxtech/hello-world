from decimal import Decimal
from math import sqrt
import os

def welcome():
    print("\n\n### Benvenuto nella Calcolatrice by Fabiux v1.0###\n")
menu_text = """
Quale operazione vuoi eseguire? Puoi scegliere tra le seguenti:
        1. Addizione
        2. Sottrazione
        3. Moltiplicazione
        4. Divisione
        5. Elevamento a potenza
        6. Radice quadrata
        7. Uscire
"""

def keepgoing():
    yesorno = input(f"\nVuoi continuare? S/N: ")
    if yesorno == "s" or yesorno == "S":
        return True
    else:
        print(f"\nCiao, alla prossima!")
        return False

def addition():
    print("Hai scelto addizione\n")
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))
    add(a,b)

def add(a,b):
    x = Decimal(a) + Decimal(b)
    print(f"Il risultato di {a} + {b} è: {x:.3n}")

def subtraction():
    print("Hai scelto Sottrazione\n")
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))
    sub(a,b)

def sub(a,b):
    x = Decimal(a) - Decimal(b)
    print(f"Il risultato di {a} - {b} è: {x:.3n}")

def multiplication():
    print("Hai scelto Moltiplicazione\n")
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))
    mult(a,b)

def mult(a,b):
    x = Decimal(a) * Decimal(b)
    print(f"Il risultato di {a} * {b} è: {x:.3n}")

def division():
    print("Hai scelto Divisione\n")
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))
    div(a,b)

def div(a,b):
    x = Decimal(a) / Decimal(b)
    print(f"Il risultato di {a} diviso {b} è: {x:.3n}")

def power():
    print("Hai scelto Elevamento a potenza\n")
    a = float(input("Inserisci il numero: "))
    b = float(input("Inserisci la potenza: "))
    pow(a,b)

def pow(a,b):
    x = a ** b
    print(f"Il risultato di {a} elevato a {b} è: {x}")

def square():
    print("Hai scelto Radice quadrata\n")
    a = float(input("Inserisci il numero: "))
    sqr(a)

def sqr(a):
    x = sqrt(a)
    print(f"La radice quadrata di {a} è: {x}")

def menu():
    while True:
        #os.system('cls' if os.name == 'nt' else "printf '\033c'")
        print(menu_text)
        select_op = input("Seleziona il numero corrispondente all'operazione desiderata: ")
        if select_op == "1":
            addition()
        elif select_op == "2":
            subtraction()
        elif select_op == "3":
            multiplication()
        elif select_op == "4":
            division()
        elif select_op == "5":
            power()
        elif select_op == "6":
            square()
        elif select_op == "7":
             print(f"\nCiao alla prossima!")
             break
        else:
            print(f"\n\n!!!Operazione non corretta!!!")
            continue
        if not keepgoing():
            break
welcome()
menu()