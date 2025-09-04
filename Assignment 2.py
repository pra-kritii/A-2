#Task 1
n = int(input("Enter an integer: "))
if n%2==0:
    print(n, "is an even number")
else:
    print(n, "is an odd number")


#Task 2
sum=0
for num in range(1,51):
    sum+=num
print("The sum of numbers from 1 to 50 is:",sum)