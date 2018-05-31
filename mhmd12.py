def count(x):
    length = len(x)
    digit = 0
    letters = 0

    for i in x:
        if i.isalpha():
            letters += 1
        elif i.isnumeric():
            digit += 1
        elif i.isspace():
            space += 1
        else:
            other += 1
    return digit,letters

print (count(input('pls enter a text: ')))