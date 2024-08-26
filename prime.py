n=int(input("enter the number:"))
count=1
for i in range(1,n):
    if(n%i==0):
        count+=1
if(count==2):
    print("it is prime number")
else:
     print("it is not a prime number")
