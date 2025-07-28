
# Q) Write a python program to test if an array contains a specific value.


arr =[29,44,58,50]

def is_check(num):
    value=int(input("enter any number:- "))
    
    if value in num:
        return True
        
    else:
        return False
        
if is_check(arr):
    print("it is correct number")
    
else:
    print("it is not correct number")