# : A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12 Your program should accept a sequence of comma
# separated passwords and will check them according to the above criteria. Passwords that match
# the criteria are to be printed, each separated by a comma. Example If the following passwords are
# given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345 Then, the output of the program should be: ABd1234@1
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
li=[x for x in input("enter passwords:").split(',')]
print("fst list: ",li)
for i in li:
    if len(i)>6 and len(i)<12:
        print(f"length okay : {i}")
    for j in i:
        if j.isalpha() is True:
            # print("ok alpha",i)
            continue
        if j.isdigit() is True:
            # print("ok digit ",i)
            continue
        if j.isupper() is True:
            print("ok upper",i)
            continue
        # if j in '$#@':
        #     continue
        if j not in '$#@':
            continue
print("success upto specifications : ",i)