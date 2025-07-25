
# Q) find the minimum number in a list

numbers=[5,3,9,7,4,55,87]

min_number=100

for i in numbers:
    if i < min_number:
        min_number=i
        
print(min_number)