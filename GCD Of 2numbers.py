def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
GCD=gcd(x,y)
print("GCD is: ",GCD)
