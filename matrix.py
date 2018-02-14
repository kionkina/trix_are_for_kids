import math


def print_matrix( matrix ):
    for i in matrix:
        print "| " + str(i[0]) + " " + str(i[1])+ " " + str(i[2]) + " |"

print_matrix([[1, 2, 3], [2, 3, 4], [4,5,6]])

def ident( matrix ):
    pass

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
