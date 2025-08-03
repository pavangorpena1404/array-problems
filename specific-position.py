
# Q) Write a python program to insert an element (specific position) into an array.


number= [12,3,49,5,8,94,66,20]
number.insert(3,100)

print(number)


# Q) this is another way without using method


number = [12, 3, 49, 5, 8, 94, 66, 20]
posision=3
element=100

new_arr=[]
for i in range(posision):
    new_arr.append(number[i])
    
new_arr.append(element)
print(new_arr)

for i in range(posision,len(number)):
    new_arr.append(number[i])
    
print(new_arr)   







