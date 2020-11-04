

def binarySearch(arr, target):
    left = 0
    right = len(arr)-1
    while right >= left:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return False


n = int(input())
n_array = input().split()
n_array.sort()

m = int(input())
m_array = input().split()

for i in m_array:
    result = binarySearch(n_array, i)
    if result != False:
        print('yes', end=' ')
    else:
        print('no', end=' ')
