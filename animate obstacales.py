import pgzrun
import itertools
import random
width = 800
height = 600
block_position = [(750,50) , (750,550) , (50,550) , (50,50)]
block_positions = itertools.cycle(block_position)
block = Actor("block" , center = (50,50))
ship = Actor("ship2" , center = (width // 2 , height // 2))

def draw():
    screen.clear()
    block.draw()
    ship.draw()

def move_block():
    animate(block , "bounce_end" , duration = 2 , pos = next(block_positions))
move_block()

clock.schedule_interval(move_block , 2)

def next_ship_target():
   x = random.randint(150,650)
   y = random.randint(150,450)
   ship.target = (x,y)
   
   target_angle = ship.angle_to(ship.target)
   target_angle += 360 * ((ship.angle - target_angle + 180) // 360)
   animate(ship , angle = target_angle , duration = 0.3 , on_finished = move_ship())

def move_ship():
    anim = animate(ship , tween = "accel_decel" , pos = ship.target ,
                    duration = ship.distance_to(ship.target) / 200 , on_finished =  next_ship_target)
next_ship_target()
pgzrun.go()