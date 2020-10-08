#Print the prime numbers which are between 1 to entered limit number (n).

list_len = int(input("Enter a number : "))
prime_num = []
for i in range(1, list_len):
    is_prime = True
    for j in range(2,i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime_num.append(i)
print(prime_num)