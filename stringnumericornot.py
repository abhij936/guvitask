def is_number(s):
    try:
        float(s)
        print("Yes")
    except:
        print("No")
s=input()
is_number(s)
