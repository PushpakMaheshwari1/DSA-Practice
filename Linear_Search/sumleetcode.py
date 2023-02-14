def sum(nums):
    n = len(nums)
    res=[nums[0]] 
    for  i in range (1,n):
        nums[i]=nums[i]+nums[i-1] # 2 + 1 =3   3+3 = 6   4+6 = 10 
        res.append(nums[i])
    return res
nums=[1,2,3,4,5]
a = sum(nums)
print(a)
