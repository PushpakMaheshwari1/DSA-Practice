# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

digits = [1,2,3]
for i in range(len(digits)):
    if i == len(digits) - 1:
        sum = 