nums = [1,2,3,4,0]
index = [0,1,2,3,0]
Final = []
n = len(nums)
for i in range(0,n):
    Final.insert(index[i],nums[i])
print(Final)