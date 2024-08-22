#input:hello world and practice makes perfect and hello world again Then, the
#output should be: again and hello makes perfect practice world
str=input("enter a string:").split(" ")
print(str)
duplicates=[]
for i in str:
    if i not in duplicates:
        duplicates.append(i)
print("after removing duplicates from the list:",duplicates)
duplicates.sort()
print(duplicates)
# ans in browser
# s = input()
# words = [word for word in s.split(",")]
# print(" ".join(sorted(list(set(words)))))