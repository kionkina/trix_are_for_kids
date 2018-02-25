from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 218, 165, 32]

cat = new_matrix()
print_matrix(cat)



'''
 YAY THIS WORKS
add_point(matrix, 300, 300, 0)
add_point(matrix, 0, 0, 0)
print "Added point"
print_matrix(matrix)
draw_lines( matrix, screen, color )
'''

#face
add_edge(cat, 250, 10, 0, 100, 250, 0)
add_edge(cat, 100, 250, 0, 400, 250, 0)
add_edge(cat, 400, 250, 0, 250, 10, 0)


#ears
add_edge(cat, 100, 250, 0, 140, 350, 0)
add_edge(cat, 140, 350, 0, 180, 250, 0)

add_edge(cat, 320, 250, 0, 360, 350, 0)
add_edge(cat, 360, 350, 0, 400, 250, 0)


#eyes
add_edge(cat, 150, 200, 0, 200, 200, 0)
add_edge(cat, 300, 200, 0, 350, 200, 0)
        

#whiskers
whiskers = new_matrix()
add_edge(whiskers, 100, 190, 0, 240, 130, 0)
add_edge(whiskers, 100, 130, 0, 240, 130, 0)
add_edge(whiskers, 100, 70, 0, 240, 130, 0)

add_edge(whiskers, 400, 190, 0, 260, 130, 0)
add_edge(whiskers, 400, 130, 0, 260, 130, 0)
add_edge(whiskers, 400, 70, 0, 260, 130, 0)


#nose
add_edge(cat, 240, 130, 0, 250, 140, 0)
add_edge(cat, 250, 140, 0, 260, 130, 0) 
add_edge(cat, 240, 130, 0, 260, 130, 0) 

#mouth
add_edge(cat, 250, 130, 0, 230, 110, 0)
add_edge(cat, 250, 130, 0, 270, 110, 0)


draw_lines(cat, screen, color )
draw_lines(whiskers, screen, color )



#print_matrix(matrix)



display(screen)
