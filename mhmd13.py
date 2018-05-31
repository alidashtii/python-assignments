def count(x):
    length = len(x)
    digit = 0
    letters = 0
    lower = 0
    upper = 0
    for i in x:
        if i.isalpha():
            letters += 1
        elif i.isnumeric():
            digit += 1
        elif (i.islower()):
            lower += 1
        elif (i.isupper()):
            upper += 1
        else:
            other += 1
    return digit,letters,lower , upper

print (count(input('pls enter a text: ')))