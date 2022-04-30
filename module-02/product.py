def mult(x,y,z):
  multiply = (x*y*z)
  return multiply

x= float(input("enter the first number :"))
y= float(input("enter the second number :"))
z= float(input("enter the third number :"))
product = mult(x,y,z)
print("the product of number : %0.1f " %product)