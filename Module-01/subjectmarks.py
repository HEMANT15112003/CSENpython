print("enter the marks of subject : ")
sub1 = int(input())
sub2 = int(input())
sub3 = int(input())
sub4 = int(input())
sub5 = int(input())

avg = (sub1 + sub2 + sub3 + sub4 + sub5)/5
if (avg>=90 and avg<=100 ):
  print("A")
elif (avg>=80 and avg<90) :
  print("B")
elif avg>=70 and avg<80 :
  print("C")
elif avg>=60 and avg<70 :
  print("D")
else: 
  print("fail")