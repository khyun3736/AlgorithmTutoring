def binarySearch(arr, S, L):                        #이진탐색
    while True:                                     #반복문
        mid = (S+L) // 2                            
        if arr[mid] < mid:                          
            S = mid + 1
        elif arr[mid] > mid:
            L = mid - 1
        else:
            return mid                              #인덱스값과 실값이 같은경우 그 값을 리턴함

        if S > L:
            return -1                               #시작값이 끝값보다 클 경우 -1 값을 리턴하고 종료


N = int(input())
arr = list(map(int, input().split()))
arr.sort()

index = binarySearch(arr,0,N-1)                     #고정점값 계산
print(index)


