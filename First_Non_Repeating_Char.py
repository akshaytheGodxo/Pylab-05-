c = input()
con1 = False
con2 = False
count = 1
ans = 0
for i in range(0 , len(c)):
    temp = c[i]
    count = 1
    for j in range(0 , len(c)):
        if temp == c[j]:
            count += 1
        else:
            pass
    if count <= 2:
        ans = i
        con1 = True
        con2 = False
        break
    else:
        con1 = False
        con2 = True


if con1 == True:
    print(c[ans])
else:
    print(None)