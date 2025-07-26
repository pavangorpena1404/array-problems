
# Q) how to find prime positive numbers only by using list comprehension

numbers = [1, 8, 9, 39, 4, -22, -82, 85, 76, 99, -30, 45, 85, 67, -2, 24, 53]

prime_numbers = [
    num
    for num in numbers
    if num > 1 and not any(num % i == 0 for i in range(2, num))
]

print(prime_numbers)


# Q) how to find prime numbers normal numbers in a list by using list comprehension 

numbers = [1, 8, 9, 39, 4, 85, 76, 99, 45, 85, 67, 24, 53]

prime_numbers = [
    num
    for num in numbers
    if not any(num % i == 0 for i in range(2, num)) and num != 1
]

print(prime_numbers)


