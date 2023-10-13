n = [str(x) for x in input().split()]
count1 = 0
count2 = 0
for i in range(0 , int(n[0])):
    for j in range(0 , int(n[2])):
        if (i+j) % 2 != 0:
            count1 += 1
        else:
            count2 += 1
    
print(count1)