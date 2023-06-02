myList = ['Mela','Banana','Fragola','Pera']

def add_list():
    print(myList)
    myitem = input(f'Cosa vuoi aggiungere?')
    myList.append(myitem)

def del_list():
    print(myList)
    myitem = input(f'Cosa vuoi eliminare?')
    myList.remove(myitem)
    
def order_list():
    which_order = input(f'in quale ordine vuoi la lista?\n 1) A-Z \n 2) Z-A?\n')
    if which_order == '1':
        order = False
    elif which_order == '2':
        order = True
    else:
        print('Non hai scelto, sarà usato il default A-Z')
        order = False
    return myList.sort(reverse=order)
order_list()
print(f'La lista è composta da:', end=' ')
for item in myList:
    print(item, end='')
#def sum_multiple_numebrs(numbers_to_sum):
#    '''Calcola la somma di più numeri.
#    I valori vengono passati come lista e poi eseguita la somma'''
#    global total
#    total = 0
#    for item in numbers_to_sum:
#        total += item
#    return total
#help(sum_multiple_numebrs)
#while True:
#    global my_numbers
#    my_numbers = []
#    numero = input('Inserisci il numero da sommare (se premi q esci)')
#    if numero == 'q':
#        break
#    else:
#        my_numbers.append(int(numero))
#        print(my_numbers)
#sum_multiple_numebrs(my_numbers)
#if total > 0:
#    print(f'La somma dei numeri da te inseriti {my_numbers} è {total}')
#else:
#    print(f'Non hai inserito alcun numero')