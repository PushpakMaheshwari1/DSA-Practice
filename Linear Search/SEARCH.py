Array=[[1,2,3,4,5],[6,7,8,11,10]]
Target = 3

def search(array):
    max = array[0][0]
    for row in range(len(Array)):
        for column in range(len(Array[row])):
            if(Array[row][column] == Target):
               return True
            else :
                return False

