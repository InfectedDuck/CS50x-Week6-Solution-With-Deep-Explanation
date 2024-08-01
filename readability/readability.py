from cs50 import get_string
letters=sentences=0
words=1
text=get_string("Text: ")
for i in range(len(text)):
    if (text[i].isalpha()):
        letters+=1
    elif text[i]==' ':
        words+=1
    elif (text[i]=='.' or text[i]=='!' or text[i]=='?'):
        sentences+=1
Li=(letters/words)*100
Si=(sentences/words)*100
index=round(0.0588*Li-0.296*Si-15.8)
if index>16:
    print("Grade 16+")
elif index<=1:
    print("Before Grade 1")
else:
    print("Grade",index)
