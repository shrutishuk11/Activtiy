N = int(input("Enter the number: "))
sum1 = 0
x = 1
#while loop
while x < N:
    if N % x == 0:
        sum1 = sum1 + x
x = x+1
if sum1 > N:
    print(N," This is the abundant number")
if sum1 == N:
    print(N," This is the perfect number")
if sum1 < N:
    print(N," This is the deficient number")