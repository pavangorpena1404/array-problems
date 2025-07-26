
# Q) find the samll-number in a list 

arr=[7,4,5,9,32,85,21,4,75]
      
small_number=float('inf')

for i in arr:
    if small_number > i:
        small_number=i
        
print(small_number)   