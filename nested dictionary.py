house = {
"Aahil" :{"age": 11 , 
          "marks" : [90 , 95 , 100 , 80]} , 
          
"Ayra" : {"age": 11 , 
          "marks" : [75 , 80 , 90 , 85]}}
print(house["Ayra"]["age"])
print(house["Aahil"]["marks"])
sent = input("Enter a sentence")
character_count = {}
for i in sent:
    if i in character_count:
        character_count[i] += 1
    else:
        character_count[i] = 1
print("Character occurences")
for char , count in character_count.items():
    print(f"{char} : {count}")