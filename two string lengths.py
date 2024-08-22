#5. Define a function that can accept two strings as input and
# print the string with maximum length in console.If two strings
# have the same length, then the function should print all strings line by line.
def str(str1,str2):
    if len(str1)> len(str2):
        print("string1 has max length",str1)
    if len(str1)<len(str2):
        print("string2 has max length",str2)
    if len(str1)==len(str2):
        print(f"{str1}oihfweiofnse\n{str2}")
str1=input("enter fst string: ")
str2=input("enter second string:")
str(str1,str2)
