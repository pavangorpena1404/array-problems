
# Q) find the even-number and odd-number in a array 

numbers=[1,8,9,39,4,-22,-82,85,76,99,-30,45,85,67,-2,24,53,] 

even_number=[]
odd_number=[]

for i in numbers:
    if 0<i:
        if i%2==0:
            print(f"this is even number {i}")  # this is called formating string 
            even_number.append(i)
        else:
            print(f"this is odd number {i}")   # this is called formating string
            odd_number.append(i)
            
            
print(even_number) 
print(odd_number)

# Q)find the even numbers in a array  List comprehension

numbers=[1,8,9,39,4,-22,-82,85,76,99,-30,45,85,67,-2,24,53,]

even_numbers=[i for i in numbers if 0<i and i%2==0]
print(even_numbers)
