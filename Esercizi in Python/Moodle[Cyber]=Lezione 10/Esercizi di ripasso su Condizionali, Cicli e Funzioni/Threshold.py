#Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.
def sum_above_threshold(numbers: list[int], limit: int) -> int:
    result: list =[]
    for i in numbers:
        if i > limit:
            result.append(i)
    return sum(result)