s = input()
arr = []
sum1 = 0

for i in range(len(s)):
    if 65 <= ord(s[i]) <= 90:
        arr.append(s[i])
    
    if 48 <= ord(s[i]) <= 57:
        sum1 += int(s[i])

arr.sort()

arr.append(str(sum1))

print(''.join(arr))