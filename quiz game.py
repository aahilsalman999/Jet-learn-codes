import pgzrun , random
title = "Quiz Master:"
width = 800
height = 800

#define rectangular areas for different elements = Rect(x,y,width,height)
marquee_box = Rect(0,0,745,75)
question_box = Rect(0,0,725,50)
timer_box = Rect(0,0,125,115)
answer_box_1 = Rect(0,0,550,50)
answer_box_2 = Rect(0,0,550,50)
answer_box_3 = Rect(0,0,550,50)
answer_box_4 = Rect(0,0,550,50)
skip_box = Rect(0,0,150,300)

#Variables
score = 0
countdown = 10
marquee_message = ""
is_game_over = False
question_file_name = "questions.txt"
answer_boxes = [answer_box_1,
                answer_box_2,
                answer_box_3,
                answer_box_4]
question = []
question_count = 0
question_index = 0

#move rectangles to their correct position on screen
marquee_box.move_ip(20,20)
question_box.move_ip(40,135)
timer_box.move_ip(645,207)
answer_box_1.move_ip(40,235)
answer_box_2.move_ip(40,335)
answer_box_3.move_ip(40,435)
answer_box_4.move_ip(40,535)
skip_box.move_ip(625,335)

def draw():
  global marquee_message
  screen.clear()
  screen.fill("Black")
  screen.draw.filled_rect(marquee_box,"yellow")
  screen.draw.filled_rect(question_box,"yellow")
  screen.draw.filled_rect(timer_box,"yellow")
  screen.draw.filled_rect(skip_box,"yellow")
  for answer_box in answer_boxes:
     screen.draw.filled_rect(answer_box,"yellow")
  marquee_message = "Welcome to Quiz Master"
  marquee_message = marquee_message + f" : {question_index} of {question_count}"
  screen.draw.textbox(marquee_message , marquee_box , color = "Black")
  screen.draw.textbox(str(countdown),timer_box , color = "Black", shadow = (0.5 , 0.5) , scolor = "yellow")
  screen.draw.textbox("Skip" , skip_box , color = "Black" , angle = -90)
  screen.draw.textbox(questions[0].strip(),question_box , color = "Black" , shadow = (0.5 , 0.5) , scolor = "yellow")
  
  #display answer choices
  index = 1
  for answer_box in answer_boxes:
     screen.draw.textbox(questions[index] , answer_box , color = "Black")
     index = index + 1
def move_marquee():
   marquee_box.x = marquee_box.x - 5
   if marquee_box.right < 0:
     marquee_box.left = width
    
def update():
   move_marquee()

def read_question_file():
  global question_count , questions
  question_file = open(question_file_name , "r" , encoding="utf-8")
  for questions in question_file:
     question.append(questions)
     question_count = question_count + 1
  question_file.close()
  
def read_next_question():
  global question_index
  if question: 
     question_index += 1
     questions = random.choice(question)
     question.remove(questions)
     return questions.split(",")
  else:
     return ("No more message", "!" , "$" , "*" , "#" , 5)
  
def on_mouse_down(pos):
   index = 1
   for box in answer_boxes:
      if box.collidepoint(pos):
         if index is int(questions[5]):
            correct_answer()
         else:
            game_over()
      index = index + 1

   if skip_box.collidepoint(pos):
       skip_question()

def correct_answer():
   global score , questions , countdown , question_count
   score = score + 1
   if question:
      questions = read_next_question()
      countdown = 10
   else:
      game_over()

def game_over():
   global questions , countdown , is_game_over
   message = f"Game Over\n You got {score} questions correct" 
   questions = [message , "!" , "$" , "*" , "#" , 5]
   countdown = 0
   is_game_over = True

def skip_question():
   global questions , countdown
   if question and not is_game_over:
      questions = read_next_question()
      countdown = 10
   else:
      game_over()
      
def update_countdown():
   global countdown
   if countdown:
      countdown = countdown - 1
   else:
      game_over()
read_question_file()
questions = read_next_question()
clock.schedule_interval(update_countdown , 1)
pgzrun.go()
