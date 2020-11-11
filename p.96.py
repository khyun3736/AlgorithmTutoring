N, M = map(int, input().split())                 #행과 열수를 입력받음
result = []                                     
for i in range(0, N):                           #행의 수 만큼 반복게산
    arr = list(map(int, input().split()))       #행에 속한 숫자를 입력받음
    arr.sort()                                  #정렬
    
    result.append(arr[0])                       #행에 속한 최솟값을 result에 삽입


result.sort(reverse = True)                     #result값을 내림차순으로 정렬
print(result[0])                                #각 행에서의 최솟값중 최대값을 출력




