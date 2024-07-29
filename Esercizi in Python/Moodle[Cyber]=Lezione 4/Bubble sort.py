import time

a=[i for i in range(1,(10**3)+1)]

def bubble(list):
    start=time.time()
    for i in range(len(list)):
     for j in range(len(list)- 1):
        if(a[j] > a[j+1]):
           Swap=(a[j])
           a[j]=a[j+1]