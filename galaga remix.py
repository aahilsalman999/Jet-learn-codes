import pgzrun , random
width = 800
height  = 600
fielder = Actor("fielder")
bat = Actor("bat")
bat.pos = width //2 , height - 60
speed = 5
speed_s = 10
fielders = []
balls = []
fielders.append(fielder)
fielders[-1].x = 20
fielders[-1].y = -100
score = 0

def display_score():
  screen.draw.text(str(score) , (50,30))

def on_key_down(key):
  if key == keys.SPACE:
     balls.append(Actor("ball"))
     balls[-1].x = bat.x
     balls[-1].y = bat.y - 50

def update():
  global score
  if keyboard.left:
    bat.x -= speed_s
  if bat.x <= 0:
    bat.x = 0
  if keyboard.right:
    bat.x += speed_s
  if bat.x >= width:
    bat.x = width
  
  for ball in balls:
    if ball.y <= 0:
      balls.remove(ball)
    else:
      ball.y -= 10
  for fielder in fielders:
      fielder.y += 5
      if fielder.y >= height:
        fielder.y = -100
        fielder.x = random.randint(50 , width - 50)
      
      for ball in balls:
        if fielder.colliderect(ball):
          score = score + 100
          balls.remove(ball)
          fielders.remove(fielder)

          #Creating new bugs
          new_fielder = Actor("fielder")
          new_fielder.x = random.randint(50 , width - 50)
          new_fielder.y = random.randint(-100 , 0 )
          fielders.append(new_fielder)

def draw():
  screen.clear()
  screen.fill("dark green")
  for ball in balls:
    ball.draw()
  for fielder in fielders:
    fielder.draw()
  bat.draw()
  display_score()
pgzrun.go()





      


