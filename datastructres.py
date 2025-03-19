test = {"name":"Aahil",
         "age": 12,
         }
print(test["name"])

#Add new key : value pair
test["country"] = "England"
print(test)
test["name"] = "AAHIL"
print(test)

test1 = {"Aahil":
         {"age":12,
          "country":"England"},
        "bob":
        {"age":12,
          "country":"England"}}
print(test1)
print(test1["Aahil"]["country"])
del(test1["Aahil"]["age"])
print(test1)
print(test1.keys())
print(test1.values())
for i in test1.keys():
  print(test1[i])
  