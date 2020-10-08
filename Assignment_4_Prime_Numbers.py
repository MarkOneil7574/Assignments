#this find if the number is prime number or not

number = int(input("Write a number to control if it's a prime number or not :   "))

for i in range(2, number):
    if (number % i == 0):
        is_prime = "is not a prime number"
        break
    else:
        is_prime = "is a prime number"
print(number,"", is_prime)