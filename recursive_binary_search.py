def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint-1],target)

def verify(index):
    if index == True:
        return print("Target found")
    else:
        return print("Target not found")


        
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
index=recursive_binary_search(list,12)
index2=recursive_binary_search(list,23)
verify(index)
verify(index2)