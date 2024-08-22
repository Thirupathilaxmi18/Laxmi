# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program: hello world! 123
# Then, the output should be: LETTERS 10 DIGITS 3
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
str=input("enter a sentence:")
cl=0
cd=0
for i in str:
    if i.isalpha() is True:
        cl=cl+1
    elif i.isdigit() is True:
        cd+=1
    else:
        pass
print("LETTERS ",cl)
print("DIGITS ",cd)