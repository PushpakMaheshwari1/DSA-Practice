class Solution(object):
   def searchRange(self, nums, target):
      res = [-1,-1]
      start = 0
      end = len(nums)
      while start<end:
         mid = int(start + (end-start)//2)
         if nums[mid] == target:
            end = mid
            res[0]=mid # [4,4], [5,5]
            res[1]=mid # s=0, e=6, e=5
         elif nums[mid]<target:
            start = mid+1 # s=4,s=5
         else:
            end = mid
      if res[0] == -1:
         return res
      start = res[0]+1
      while start<end:
         mid = int(start + (end-start)//2)
         if nums[mid] == target:
            start = mid+1
            res[1] = mid
         elif nums[mid] < target:
            start = mid + 1
         else:
            end = mid
      return res
ob1 = Solution()
print(ob1.searchRange([2,2,2,3,3,4,4,4,4,5,5,6], 4))