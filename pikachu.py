import pgzrun
import random
width = 600
height = 500
score = 0
game_over = False
pikachu = Actor("pikachu")
pikachu.pos = 100 , 100
ash = Actor("ash")
ash.pos = 200 , 200
def draw():
  screen.blit("space" , (0 , 0))
  ash.draw()
  pikachu.draw()
  screen.draw.text("Score: " + str(score) , color = "white" ,  topleft = (0,0) , fontsize = 40)
  if game_over:
    screen.fill("pink")
    screen.draw.text("Time's Up! Your final score is: " + str(score) , midtop = (width/2 , 10) , fontsize = 40 , color = "red")

def place_ash():
   ash.x = random.randint(70 , (width - 70))
   ash.y = random.randint(70 , (height - 70))

def time_up():
    global game_over
    game_over = True

def update():
    global score
    if keyboard.left:
      pikachu.x = pikachu.x - 2
    if keyboard.right:
      pikachu.x = pikachu.x + 2
    if keyboard.up:
      pikachu.y = pikachu.y - 2
    if keyboard.down:
      pikachu.y = pikachu.y + 2
    ash_collected = pikachu.colliderect(ash)
    if ash_collected:
       score = score + 10
       place_ash()
clock.schedule(time_up , 60)
pgzrun.go()

       


     
  

