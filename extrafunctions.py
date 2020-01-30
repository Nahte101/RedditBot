
def checkTimeArraysEqual(arr1,arr2):#must be of same length
    match = True
    for i in range(0,len(arr2)):
        if int(arr1[i]) != int(arr2[i]):
            match = False
            break
    return match