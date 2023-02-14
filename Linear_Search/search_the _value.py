lst = [1,2,3,4,5,6,7,8,9]
target = 3

def search(lst,target):
    start = 0
    end = len(lst) - 1

    while(start <= end):
        mid = (start + (end - start)//2)
        print("current middle value",lst[mid])
        if (target < lst[mid]): # search left hand side
            end = mid - 1
        elif(target > lst[mid]): # search right hand side
            start = mid + 1
        else:
            return mid
    return -1 

a = search(lst,target)
print(a)