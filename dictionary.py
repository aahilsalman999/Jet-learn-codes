food = {"Num1" : "Pizza" , "Num2" : "Burger" , "Num3" : "fries" , "Num4" : "chicken"}
#print(food["Num"])
print(food.get("Num","unkown"))
food["Num"] = "crisps"
print(food["Num"])
print(food.keys())
print(food.values())
print(len(food))
print("Num10"in food)
print("Num10" not in food)
del food["Num1"]
print(food)
food["Num2"] = "banana"
print(food)
menu = []
for i in food:
    menu.append(i)
menu.sort()
print(menu)
