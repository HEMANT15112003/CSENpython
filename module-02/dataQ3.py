'''# programm to find second smallest and second largest number 
def find_len(list1):
    length = len(list1)
    list1.sort()
    
    
    print("Second Largest element is:", list1[length-2])
    print("Second Smallest element is:", list1[1])
  
# Driver Code
list1=[12, 45, 2, 41, 31, 10, 8, 6, 4]
Largest = find_len(list1) '''


def Range(list1): 
    largest = list1[0] 
    lowest = list1[0] 
    largest2 = None
    lowest2 = None
    for item in list1[1:]:     
        if item > largest: 
            largest2 = largest
            largest = item 
        elif largest2 == None or largest2 < item: 
            largest2 = item 
        if item < lowest: 
            lowest2 = lowest
            lowest = item 
        elif lowest2 == None or lowest2 > item: 
            lowest2 = item 
              
    
    
    print("Second Largest element is:", largest2) 
    print("Second Smallest element is:", lowest2) 
  
  
# Driver Code
list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4]
Range(list1)
