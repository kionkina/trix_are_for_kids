import math


def print_matrix( matrix ):
    len_row = len(matrix)
    len_col = len(matrix[0])

    print "len_row: " + str(len_row)
    print "len_col: " + str(len_col)
    ret = ""
    for r in range(len_row):
        ret += "|"
        for c in range(len_col):
             ret +=  " " + str(matrix[r][c])
        ret +=  " |" + " \n" 
    print ret 

#print_matrix([[1, 2, 3], [2, 3, 4], [4,5,6]])

def ident( matrix ):
    ret = []
    len_row = len(matrix)
    len_col = len(matrix[0])
    for r in range(len_row):
        new_row = []
        for c in range(len_col):
            if (c == r):
                new_row.append(1)
            else:
                new_row.append(0)
        ret.append(new_row)
    return ret

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    ret = [] # 2D array to return
    inner = len(m2)
    place_in_row = len(m2[0])
    for row in range(len(m1)):
        new_row = []
        for p in range(place_in_row): #this is the number of columns in m2
            sum = 0
            for i in range(len(m2)): #cols of m1
                sum += m1[row][i]* m2[i][p]
            new_row.append(sum)
        ret.append(new_row)
    return ret

#print matrix_mult([[1, 2],[3, 4]], [[2,0], [1,2]])
#print matrix_mult([[4, 5, 6], [7, 8, 9], [10, 11, 12]], [[1,2,3],[4,5,6],[7,8,9]])

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
