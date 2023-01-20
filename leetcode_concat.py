nums =[1,2,3]
def getConcatenation(nums):
        n=len(nums)
        l=[]
        for i in range(0,n):
            l.insert(i,nums[i])
            print(l)
            l.insert(i+n,nums[i])
            print(l)
        return l
a = getConcatenation(nums)
print(a)
