string=input("enter the string to be processed:")
print(len(string))
digitcount=0
lettercount=0
for i in string:
    if i.isdigit():
        digitcount=digitcount+1
    if i.isalpha():
        lettercount=lettercount+1
print("number of digits in given string is:",digitcount)
print("number of letters in given string is:",lettercount)
print("number of words in given string is:",len(string.split()))