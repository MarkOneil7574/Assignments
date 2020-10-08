#this creates a list consisting of Fibonacci Numbers

fib_list = [1,1]
i = 0
while True:
    fib_list.append(fib_list[i] + fib_list[i+1])
    i += 1
    if fib_list[i+1] >= 55:
        break
print(fib_list)