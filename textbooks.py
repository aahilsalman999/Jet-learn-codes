books = {"Physics" : "175" , "Chemistry" : "210" , "Biology" : "195" , "Maths" : "125" , "English" : "125"} 
books["Physics"] = "200"
num1extra_book = input("Select one more book")
num2extra_book = input("Select another book")
for i in books:
 books.append(i)
books[num1extra_book] = "130"
books[num2extra_book] = "130"
print(books)
