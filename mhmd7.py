
lines = []
while True:
    word = input('enter lines of words : ')
    if word:
        lines.append(word.upper())
    else:
        break;

for sentence in lines:
    print (sentence)