def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint -1
    return 0

def verify(index):
    if index != 0:
       return print("target found at the index: ", index)
    return print("target not found")

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
index= binary_search(list,12)
index2= binary_search(list,19)
verify(index)
verify(index2)