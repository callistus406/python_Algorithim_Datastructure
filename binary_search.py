
from more_itertools import last


array = [1,2,4,5,6,7,8,9,34]
def binary_search(list, target):
    first=0
    last=len(list)-1

    while (first <=last):
        midpoint = (first +last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint +1
        else:
            last = midpoint - 1
    return None

result = binary_search(array,12)
def verify(result):
    if result:
        print(f"target found at index {result}")
    else:
        print("target not found")

verify(result)      
# print(binary_search(array,8) )   

