a, b = map(int, input().split())

count = 0
while a != b:
    count += 1
    if abs(a-b) >= 10:
        if a > b:
            a -= 10
        else:
            a += 10
    
    elif abs(a-b) >= 5:
        if a > b:
            a -= 5
        else:
            a += 5
    else:
        if a > b:
            a -= 1
        else:
            a += 1
    
print(a)
print('최소횟수 : ', count)
