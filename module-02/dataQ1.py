''' programm to print a specific list after removing the 0th , 4th amd 5th elements.
sample list : ["red", "green", "white", "black", "pink", "yellow"]
expected output  : ["green", "white", "black"]'''

L1 = ['Red', 'Green', 'whte', 'black', 'pink', 'yellow']
L2 = []
print(len(L1))
for i in range(len(L1)):
  if((i==0)or (i==4) or (i==5)):
    continue
  else:
    L2.append(L1[i])
print(L2)