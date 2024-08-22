c=50
h=30
d=[x for x in input("enter numbers:").split(",")]
ans=[]
for i in d:
    x=str(int(float((((2*c*float(i))/h)**0.5))))
    ans.append(x)
print("ans:",ans)