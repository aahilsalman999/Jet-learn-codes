import pgzrun , random
title = "Quiz Master:"
width = 800
height = 800

#define rectangular areas for different ui elements = Rect(x,y,width,height)
marquee_box = Rect(0,0,700,50)
question_box = Rect(0,0,400,50)
timer_box = Rect(0,0,100,100)
answer_box_1 = Rect(0,0,200,100)
answer_box_2 = Rect(0,0,200,100)
answer_box_3 = Rect(0,0,200,100)
answer_box_4 = Rect(0,0,200,100)
skip_box = Rect(0,0,50,200)

#Variables
score = 0
countdown = 10
marquee_message = ""
is_game_over = False
question_file_name = "question.txt"
answer_boxes = [answer_box_1,
                answer_box_2,
                answer_box_3,
                answer_box_4]
question = []
question_count = 0
question_index = 0

#move rectangles to their correct position on screen
marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
answer_box_1.move_ip(40,200)
answer_box_2.move_ip(40,300)
answer_box_3.move_ip(40,400)
answer_box_4.move_ip(40,500)
skip_box.move_ip(700,300)

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
  marquee_message = marquee_message + f"Q : {question_index} of {question_count}"
  