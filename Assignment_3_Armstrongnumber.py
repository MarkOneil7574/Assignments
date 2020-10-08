number = input("write an positive integer number")
while not(number.isdigit()):   
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    number = input("write an positive integer number") 
armnumber = int(number)
list1 = list(number)
top = len(list1)
total = 0
for i in list1:
    i = int(i)
    total += (i**(top))     
if armnumber == total:
    print(f"{armnumber} is an Armstrong number")
else :
    print(f"{armnumber} is not an Armstrong number")
