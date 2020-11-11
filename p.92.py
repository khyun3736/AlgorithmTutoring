N, M, K = map(int, input().split())

arr = []
arr = list(map(int, input().split()))

arr.sort(reverse = True)

count = 0
result = 0
for i in range(M):                  #M번 더해준다
    if count != K:                  #최대값을 더해줌
        result += arr[0]
        count += 1
    else:                           #K번 더했을때 그 다음 최대값을 더해줌
        result += arr[1]
        count = 0                   #카운트 0으로 초기화

print(result)
