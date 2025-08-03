
# Q) Write a Java program to find the index of an array element.

numbers=[10,40,3,9,5,22,14]
num=int(input("Enter any number:-"))

def check(arr,value):
    
    if value in arr:
        return True
    
    
    else:
        return False
    

if check(value=num,arr=numbers):
    index=numbers.index(num)
    print(f"index number is:- {index}")
    
else:
    print("it is invalid number")
