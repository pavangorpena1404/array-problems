
# Q) finde the large-number in a list 

arr=[2,7,4,5,9,32,85,21,4,75]

large_number=arr[0]

for i in arr:
    if large_number < i:
        large_number=i
        
print(large_number)        
