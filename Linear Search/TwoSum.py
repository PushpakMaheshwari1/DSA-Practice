# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

nums = [3,2,4]
n = len(nums)
target = 6
for i in range(n):
    for j in range (i,n):
        if nums[i] + nums[j] == target:
            print([i,j])
