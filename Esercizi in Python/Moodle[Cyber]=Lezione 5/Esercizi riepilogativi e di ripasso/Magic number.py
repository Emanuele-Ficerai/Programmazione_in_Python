#Scrivi una funzione che, dato un numero intero, determina se è un "numero magico". 
#Un numero magico è definito come un numero che contiene il numero 7.

def is_magic_number(num: int) -> bool:
    num: str=f"{num}"
    for i in num:
        if i == '7':
            return True
    return False   

print(is_magic_number(125748))