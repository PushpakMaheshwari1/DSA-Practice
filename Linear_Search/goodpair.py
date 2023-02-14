# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

nums = [5,6,7,5,5,7]
count = 0
n = len(nums)
for i in range(n):
    for j in range(i+1,n):
        if (nums[i] == nums[j]):
            count+=1
print(count)