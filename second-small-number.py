
# Q) find the second-smallest number in a list 

#  minimum = float('inf')   => it is called largest number like big number named infinity

arr=[4,22,43,6,8,55,41,28]
minimum=60

second_small=0
for i in arr:
    # print(arr[i])
    if minimum > i:
        second_large=minimum
        minimum=i
        
    elif minimum < i and second_large > i:
        second_large=i
    
print(second_large) 

# Q) this is second way 

arr=[7,4,9,32,85,21,8,75]

small_number=float('inf')
second_small=0

for i in arr:
    if small_number > i:
        second_small=small_number
        small_number=i
        
    elif small_number < i and second_small > i:
        second_small=i
        
print(second_small)       