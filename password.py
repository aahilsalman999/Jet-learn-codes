system = {"User1" :"1233211" , "User2" :"11111154",
          "User3" :"1111121" , "User4" :"11113122",
          "User5" :"1411511" , "User6" :"11111231",
          "User7" :"1111119" , "User8" :"11111134",
          "User9" :"1145111" , "User10":"11111129"}
username = input("Enter username")
if username in system:
 print("Username is found")
 password = (input("Enter password"))
 if password == system[username]:
  print("Logged in")
 else:
  print("Ivalid password")
else:
 print("Invalid username")
 