import matplotlib.pyplot as plt
q=float(input("enter charge density: "))
r=float(input("enter power of charge density , enter zero if exists: "))
m=q*pow(10,r)
y=m/17.7
z=y/pow(10,-12)
print("the value of electric field intensitry is: ",z)
plt.axhline(z)
plt.title("Variation of Electric field due to infinitly charged sheet")
plt.xlabel("Distance")
plt.ylabel("Electric field intensity")
plt.show()