1.

def maxnum():
   a=int(input("enter number1  "))
   b=int(input("enter number2  "))
   c=int(input("enter number3  "))
   print("maximum number",max(a,b,c))
maxnum()
2.

def reverse(x):
  return x[::-1]

t = reverse("pyhton")

print(t)


3.


def prime():
    a=int(input("enter number"))
    count=0
    for i in range(2,a):
        if a%i==0:
            count=count+1
        
    if count==0:
        print("prime number")
    else:
        print("composite number")
prime()


5.


def square():
    sum=0
    a=int(input("enter a positive number"))
    for i in range(1,a+1):
        sum=sum+(i*i)
    print("sum of squares",sum)
square()
     

