
# Q) reverse array 

numbers=[5,3,9,7,4,55,87]
reverse=[]

for i in range(len(numbers)-1,-1,-1):
    reverse.append(numbers[i])
    
print(reverse)   