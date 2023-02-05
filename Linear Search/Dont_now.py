lst = [9,8,7,6,5,4,3,2,1]
target = 3

def search(lst,target):
    start = 0
    end = len(lst) - 1

    if(lst[start]<lst[end]):
         isAsc = True
    else:
        isAsc = False


    while(start <= end):
        mid = (start + (end - start)//2)
        if(target == lst[mid]):
            return mid
        if(isAsc):                      # for Ascending
            if (target < lst[mid]):     # search left hand side
                end = mid - 1
            elif(target > lst[mid]):    # search right hand side
                start = mid + 1
        else:                           #for Descending
            if (target > lst[mid]):     # search right hand side
                end = mid - 1
            elif(target < lst[mid]):    # search left hand side
                start = mid + 1
    return -1 

a = search(lst,target)
print(a)