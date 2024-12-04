import pgzrun
import random
width = 300
height = 300
def draw():
    screen.clear()
    center_x , center_y = width//2 , height//2
    line_length = 150
    for i in range(20):
     r = random.randint(100,250)
     g = random.randint(100,250)
     b = random.randint(100,250)
     end_x = random.randint(0,width)
     end_y = random.randint(0,height)
     screen.draw.line((center_x,center_y),(end_x,end_y),(r,g,b))       
pgzrun.go()