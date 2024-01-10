# selection sort

new_list=[13,46,24,52,20,9]

for i in range(len(new_list)):
  minpos=i
  for j in range(i,len(new_list)):
    if new_list[j]<new_list[minpos]:
      minpos=j
      
  new_list[i],new_list[minpos]=new_list[minpos],new_list[i]

print(new_list)
      
print()

print('---------------------------------')