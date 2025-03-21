def details():
  name = input("What is your name?")
  maths = int(input("What are your maths marks?"))
  science = int(input("What are your science marks?"))
  history = int(input("What are your history marks?"))
  return name , maths , science , history

def total_average(maths , science , history):
  total = maths + science + history
  average = total / 3
  return total , average

def grades(average):
  if average > 90 and average <= 100:
    print("A")
  elif average > 70 and average <= 90:
    print("B")
  elif average > 60 and average <= 70:
    print("C") 
  elif average > 50 and average <= 60:
    print("D")
  elif average > 40 and average <= 50:
    print("E")
  else:
    print("F")

def print_marksheet(name,maths,science,history,total,average):
  print("Marksheet:")
  print("Name: ",name)
  print("Maths marks:",maths)
  print("Science marks:",science)
  print("History marks:",history)
  print("Total scored:",total)
  print("Average:",average)
name,maths,science,history = details()
total,average = total_average(maths , science , history)

print_marksheet(name,maths,science,history,total,average)
print("Grades:",end=" ")
grades(average)


  
  
