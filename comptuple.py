def get_group_details():
  group_name = input("Enter the group name")
  group_venue = input("Enter group venue") 
  group_size = int(input("Enter size of group"))
  date = input("Enter date of competition")
  type_of_medal = input("Enter type of medal won") 
  return group_name , group_venue , group_size , date , type_of_medal 

def main():
  group_details = []    
  print("Enter the details for the five groups")
  for i in range(1,5):
    print(f"group{i}")
    group_tuple = get_group_details()
    group_details.append(group_tuple)
  print(group_details)
main()