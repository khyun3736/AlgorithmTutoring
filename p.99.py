N, K = map(int, input().split())
count = 0;
while N != 1:                        #N이 1이 아니면 계속 반복
    if N % K == 0:                   #N이 K로 나눠지면 나누고 카운트+1
        N = N / K
        count += 1
    else:                            #나눠지지 않으면 1을 빼고 카운트+1
        N -= 1
        count += 1

print(count)                         #카운트출력

