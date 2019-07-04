s=input()
special=0
for i in range(len(s)) :
    if(s[i].isalpha()) :
        continue
    elif(s[i].isdigit()) :
        continue
    else :
        special=special+1
print(special)
