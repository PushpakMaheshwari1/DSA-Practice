# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

from itertools import chain
def shuffle(a,n):
        return chain(*zip(a[:n], a[n:]))  ## Here Inside zip two list created [2,5,1] AND [3,4,7] . 
                                          ## Now using zip it pair the two list like [2,3] [5,4] [1,7].
                                          ## And Chain will chain the two paired list.
        
