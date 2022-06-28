def linear_search(list, target):
    """ 
    search the list for a target value
     """
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return 0

def verify(index):
    if index != 0:
       return print("target found at the index: ",index)
    return print("target not found")

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
index=linear_search(list,12)
verify(index)