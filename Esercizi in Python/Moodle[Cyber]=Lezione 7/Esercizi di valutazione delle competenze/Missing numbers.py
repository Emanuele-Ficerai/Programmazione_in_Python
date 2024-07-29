#print(find_disappeared_numbers([4,3,2,7,8,2,3,1])) [5, 6]
def find_disappeared_numbers(nums: list[int]) -> list[int]:
    numeri: list=[]
    n: int= len(nums)
    for i in range(1, n+1):
        if i not in nums:
            numeri.apppend(i)
    return numeri