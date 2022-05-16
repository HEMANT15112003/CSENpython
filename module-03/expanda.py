import pandas as pd
# print(pd.__version__)#

d = {'Branch' : ['EEE', 'CSE', 'ECE', 'MECH'],'STUDENTS' : [12,120,50,20]}
m = pd.DataFrame(d)
print(m)