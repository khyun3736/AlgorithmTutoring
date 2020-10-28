
####################


def Desc_Sort(arr, N):
    for i in range(N, 0, -1):
        for j in range(0, i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


####################


N = int(input(''))
arr = []
for i in range(0, N):
    arr.append(int(input('')))
print('결과 :', Desc_Sort(arr, N))
