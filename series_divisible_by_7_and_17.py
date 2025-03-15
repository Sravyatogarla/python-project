#PROBLEM STATEMENT-3

#Create a list to store the numbers divisible by 7 and 17
numbers =[]

#iterate through numbers from 1 to 1000
for num in range(1, 1000):
    if num% 7==0 and num%17==0:
        numbers.append(num)
print(numbers)
