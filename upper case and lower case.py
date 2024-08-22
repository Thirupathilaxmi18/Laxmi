# 4. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#Suppose the following input is supplied to the program: Hello world!
#Then, the output should be: UPPER CASE 1 LOWER CASE 9
str=input("enter a sentence(default Hello world!):")
countforupper=0
countforlower=0
for i in str:
    if i.isupper() is True:
        countforupper+=1
    if i.islower() is True:
        countforlower+=1
print("UPPER CASE ", countforupper)
print("LOWER CASE ",countforlower)