#Data una lista di numeri interi, riordina i numeri in modo che tutti i numeri pari appaiano prima di tutti i numeri dispari. 
#Restituisce l'elenco riorganizzato.
def even_odd_pattern(nums: list[int]) -> list[int]:
    c=0
    for i in range(len(nums)):
        if nums [i] % 2==0:
            k=nums[i]
            nums.remove(k)
            nums.insert(c, k)
            c=c+1
    return nums