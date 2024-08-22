def fact(n):
    for i in range(n):
        if n==0:
            return 1
        elif n==1:
            return 1
        else:
            return n*fact(n-1)
n=int(input("enter the range:"))
print(f"factorial of {n}:{fact(n)}")
