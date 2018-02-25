from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    i = 0
    while (i < len(matrix[0])):
       draw_line(matrix[0][i], matrix[1][i], matrix[0][i+1], matrix[1][i+1], screen, color)
       i += 2
    print "done drawing"

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    matrix[0].append(x0)
    matrix[0].append(x1)
    matrix[1].append(y0)
    matrix[1].append(y1)
    matrix[2].append(z0)
    matrix[2].append(z1)
    matrix[3].append(0)
    matrix[3].append(0)
    
def add_point( matrix, x, y, z=0 ):
    matrix[0].append(x)
    matrix[1].append(y)
    matrix[2].append(z)
    matrix[3].append(0)



def draw_line( x0, y0, x1, y1, screen, color ):
    print "DRAWING LINE FROM " + str(x0) + " " + str(y0) 
    print "TO " + str(x1) + " " + str(y1)
    # OCTANT 
    A = y1-y0
    B = -1*(x1-x0)
#swapping x and y coordinates if x is decreasing to use same formula for different 
    if B >= 0:
        oldx1 = x1
        oldy1 = y1
        oldx0 = x0
        oldy0 = y0
        x1 = oldx0
        y1 = oldy0
        x0 = oldx1
        y0 = oldy1
    x = x0
    y = y0
    A = y1-y0
    B = -1*(x1-x0)
    plot(screen, color, x0, y0)
    #OCTANT I and V ==> the slope is less than or equal to one and positive                                     
    if (A>0 and B<=0 and A<=-B):
        d=2*A+B
        while (x < x1):
            plot(screen, color, x, y)
#            print "x: "+str(x)
#            print "y: "+str(y)
            if (d > 0):
                y+=1
                d+=(2*B)

            x+=1
            d+=(2*A)
#OCTANT II and VI
    elif (B<=0 and A>=0 and A>=-B):
#        print "case 2 ------"
        d=2*B+A
        while (y < y1):
            plot(screen, color, x, y)
#            print "x: "+str(x)
#            print "y: "+str(y)
            if (d<0):
                x+=1
                d+=2*A
            y+=1
            d+=2*B
    #OCTANT III and VII ==> slope is between -1 
    elif (A<=0 and B<=0 and -A>=-B): #realized this is not the same as A<=
        print "case 3 -----"
        d=(-2*B)+A
        while (y > y1):
            plot(screen, color, x,y)
#            print "x: "+str(x)
#            print "y: "+str(y)
            if (d>0):
                x+=1
                d+=2*A
            y-=1
            d-=2*B
    #VIII and IV slope is less than -
    else:
        d=2*A-B
        while(x<x1):
            plot(screen,color,x,y)
            if(d<0):
                y-=1
                d-=2*B
            x+=1
            d+=2*A
    plot(screen, color, x1, y1)
#    print "x1: " + str(x1)
#    print "y1: " + str(y1)



    
