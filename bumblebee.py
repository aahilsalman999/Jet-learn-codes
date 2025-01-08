import pgzrun
import random
width = 600
height = 500
score = 0
game_over = False
bee = Actor("bee")
bee.pos = 100 , 100
flower = Actor("flower")
flower.pos = 200 , 200
def draw():
  screen.blit("space" , (0 , 0))
  flower.draw()
  bee.draw()
  screen.draw.text("Score: " + str(score) , color = "white" ,  topleft = (0,0) , fontsize = 40)
  if game_over:
    screen.fill("pink")
    screen.draw.text("Time's Up! Your final score is: " + str(score) , midtop = (width/2 , 10) , fontsize = 40 , color = "red")

def place_flower():
   flower.x = random.randint(70 , (width - 70))
   flower.y = random.randint(70 , (height - 70))

def time_up():
    global game_over
    game_over = True

def update():
    global score
    if keyboard.left:
      bee.x = bee.x - 2
    if keyboard.right:
      bee.x = bee.x + 2
    if keyboard.up:
      bee.y = bee.y - 2
    if keyboard.down:
      bee.y = bee.y + 2
    flower_collected = bee.colliderect(flower)
    if flower_collected:
       score = score + 10
       place_flower()
clock.schedule(time_up , 60)
pgzrun.go()

       


     
  

