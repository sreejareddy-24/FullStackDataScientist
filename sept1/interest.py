k0=int(input("Enter the initial balance:"))
rate=int(input("enter the annual interest rate:"))
years=int(input("Enter the number of years:"))

n=1
while n<=years:
    kn=k0*((1+(rate/100))**n)
    print(f"interest after {n} years is:{kn:.2f}")
    n+=1

print(f"final interest after {years} is:{kn:.2f}")