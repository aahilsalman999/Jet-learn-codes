books = {"Physics" : "175" , "Chemistry" : "210" , "Biology" : "195" , "Maths" : "125" , "English" : "125"} 
books["Physics"] = "200"
print(books)
books["History"] = "130"
books ["Geography"] = "130"
print(books)
user_book = input("Select a book")
if user_book in books:
 print("The cost of",user_book, "is",books[user_book])
else:
 print("Book not found")
for book,cost in books.items():
 print(book,cost)