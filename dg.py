def hALF(s):
    l=len (s)
    b=round(l/2)
    s1=""
    for i in range(0,b):
        s1=s1+s[i]
    print(s1)
s=input()
hALF(s)