matrix = [[1,2,3],[4,5,6],[7,8,9]]
def transpose(matrix):
        l=[]
        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            l.append(temp)
            print(l)
        return l
a = transpose(matrix)
print(a)
