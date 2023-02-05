lst = [2,3,5,9,14,16,18]
target = 20

def ceiling(lst,target):
    if (target > lst[len(lst)-1]):
        return -1
    start = 0
    end = len(lst) - 1
    while(start <= end):
        mid = (start + (end - start)//2)
        if (target < lst[mid]): # search left hand side
            end = mid - 1
        elif(target > lst[mid]): # search right hand side
            start = mid + 1
        else:
            return mid
    return start

a = ceiling(lst,target)
print(a)