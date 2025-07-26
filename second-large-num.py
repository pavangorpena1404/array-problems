
# Q) find the second large number in a list 

arr=[5,3,22,43,6,8,55,41,28]
maximum=1

second_large=0
for i in arr:
    # print(arr[i])
    if maximum < i:
        second_large=maximum
        maximum=i
        
    elif maximum > i and second_large < i:
        second_large=i
    
print(second_large) 

# Q) this is second way 

arr=[2,7,4,5,9,32,85,21,4,75]

big_number=arr[0]
second_large=1

for i in arr:
    if big_number < i:
        second_large=big_number
        big_number=i
        
    elif big_number > i and second_large < i:
        second_large=i
        
print(second_large)        