# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

matrix = [  [3,7,8],
            [9,11,13],
            [15,16,17]  ]
final = [0,0]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i]  > matrix[i] + matrix[j]:
            if matrix[j] <+ matrix[i] + matrix[j]:
                print(final)    