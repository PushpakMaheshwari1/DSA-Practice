from collections import Counter ## COUNT THE NUMBER OF ALPHABET. FOR EXAMPLE APPLE A:1  P:2 L:1 E:1
nums = [2,2,2,3,3,1,1,4]
def singleNumber(nums):
    c=Counter(nums)
    for i in nums:
        if c[i]==1:
            return i
a = singleNumber(nums)
print(a)