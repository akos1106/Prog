#43-as feladat

def substring(s,t):
    for betu in t:
        if betu not in s:
            return ""
    #ha nincs s-ben a t összes betűje, akkor biztosan nem jó

    if len(s)<len(t):
        return ""
    #ha s rövidebb mint t akkor biztosan nem jó

    osszessubstring=[]
    for i in range(len(s)):
        for j in range(i,len(s)):
            osszessubstring.append(s[i:(j+1)])
    #megvan az összes substringje az s-nek

    josubstringek=[]
    for subs in osszessubstring:
        joe=0
        for betu in t:
            if betu in subs:
                joe+=1
        if joe==len(t):
            josubstringek.append(subs)
    #az összes substring megvan, amiben benne van a t összes betűje

    return min(josubstringek,key=len)
    # megvan a legrövidebb substring amiben benne van t összes betűje

#MAIN
s="ADOBECODEBANC"
t ="ABC"

s2="x"
t2="xx"

s3="helloworld"
t3="lwr"

print(substring(s,t))
print(substring(s2,t2))
print(substring(s3,t3))