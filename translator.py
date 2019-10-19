x=(input("Enter your word: "))
word=""
for i in x:
    if i.lower() in "aeiou":
        if i.isupper():
            word=word + "G"
        else:
            word = word + "g"
    else:
        word=word + i
print(word)