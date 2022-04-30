# # mathplot.lib
# import matplotlib.pyplot as plt
# import numpy as np

# # x = np.linspace(1,20)
# #print(x)
# #plt.plot(x,y)
# # #plt.show()
# x = np.array(["CSE", "ECE", "CIVIL", "MECH"])
# y = np.array([600,300,100,100])

# # plt.bar(x,y,width = 0.4, color = "green")
# plt.pie(y)
# plt.show()
# import numpy as np
import matplotlib.pyplot as plt

fig,ax= plt.subplots()
ax.set(xlim= (-1,1),ylim = (-1,1))
a_circle = plt.Circle((0,0), 0.5, color ="red")
ax.add_artist(a_circle)
plt.show()