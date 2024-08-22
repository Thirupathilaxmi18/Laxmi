#1.For a given string, remove all duplicate characters from that string.Take the string from user input
str=input("enter a input string:")
duplicates=''
count=0
for i in str:
    if i not in duplicates:
       duplicates=duplicates+i
print(duplicates)