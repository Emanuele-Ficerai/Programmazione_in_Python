#Scrivi una funzione che rimuove tutti i duplicati da una lista, 
#contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.
lst: list=["s", "5", "v", "3"]
def remove_duplicates(lst) -> list:
    mylist: list= []
    for i in lst:
        if i not in mylist:
            mylist.append(i)
    return mylist

print(remove_duplicates(lst))