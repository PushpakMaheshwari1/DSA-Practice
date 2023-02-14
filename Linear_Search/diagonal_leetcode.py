mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

n = len(mat)-1
 
diagonal = 0
for row in range(len(mat)):
    for column in range(len(mat[row])):
       if(row == column or (row + column) == (len(mat)-1)):
        diagonal = diagonal + mat[row][column]
        print(diagonal)
    
print(diagonal)
 



