''' programm to get differnce between two list '''

L1 = ['ECE', 'CSE', 'Mech', 'Civil']
L2 = ['EEE', 'ECE', 'CSE', 'Bio']

print("Adding 2 list: ")
print(L1 + L2)
'''print("substraction 2 list: ")
print(list(set(L1) - set(L2)))'''

L3 = []
for i in L1:
  for j in L2:
    if(j==1):
      L2.remove(j)
    else:
      continue
print("substracting two list : ")
print(L1 + L2)
