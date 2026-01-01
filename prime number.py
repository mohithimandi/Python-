num = int(input("Enter a number: "))
flag = True

if num <= 1:
    flag = False

for i in range(2, num):
    if num % i == 0:
        flag = False
        break

if flag:
    print("Prime number")
else:
    print("Not a prime number")