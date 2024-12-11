metric = [[1,2,3],[4,5,6],[7,8,9]]
print(len(metric))
print(len(metric[0]))
print(metric[1][0])
print(metric[2][2])
for i in range(0,len(metric)):
  for j in range(0,len(metric[0])):
    print(metric[i][j],end=" ")
  print("\n")