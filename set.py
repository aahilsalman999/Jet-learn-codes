value  =  [1,1,2,2,3,3]
sample_set = set(value)
#print(sample_set[2])
if 4 in sample_set:
  print("yes")
else:
  print("no")
my_set  = set([])
my_set.add(3)
my_set.add(3)
my_set.add(2)
my_set.add(3)
print(my_set)
my_set.remove(2)
print(my_set)
my_set.discard(5)
print(my_set)
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
