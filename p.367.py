def binarySearch(arr, search_key, N):                        #이진탐색
    left = 0
    right = N-1
    while right >= left:
        mid = int((left + right) / 2)
        if arr[mid] == search_key:
            return mid
        if arr[mid] > search_key:
            right = mid - 1
        else:
            left = mid + 1

    return -1

N, X = map(int, input().split())                             #N, X값과 배열 입력받고 정렬
arr = list(map(int, input().split()))
arr.sort()

Target_index =  binarySearch(arr, X, N)                      #타깃의 인덱스 저장

if Target_index == -1:                                       #타깃이 없는경우 count = -1
    count = -1

else:
    count = 1                                                #타깃과 X가 일치하므로 count+1
    sub_index = Target_index                                 #서브인덱스 지정
    while True:                                              #타깃인덱스 앞에 중복된 수를 카운트 
        sub_index -= 1
        if arr[sub_index] == X:
            count += 1
        else:
            break
    add_index = Target_index                                 #애드인덱스 지정
    while True:                                              #타깃인덱스 뒤에 중복된 수를 카운트
        add_index += 1
        if arr[add_index] == X:
            count += 1
        else:
            break
                

print(count)
        







