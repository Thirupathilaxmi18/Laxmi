#  Write a program that computes the net amount of a bank account
#  based a transaction log from console input. The transaction log
#  format is shown as following: D 100 W 200 D means deposit while W means withdrawal.
#  Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100
#  Then, the output should be: 500
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
d=input("enter deposite amount:").split(",")
w=input("enter withdraw amount:").split(",")
# print(d)
# print(w)
add=0
sub=0
for i in d:
    add=add+int(i)
for i in w:
    sub=sub+int(i)
netamount=add-sub
# print("add: ",add)
# print("sub: ",sub)
print("netamount: ",netamount)