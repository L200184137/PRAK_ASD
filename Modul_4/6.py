A = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]

def binSe(target):
    low = 0
    high = len(A)

    while low < high:
        mid = (high + low) // 2
        if A[mid] == target:
            return "Target pada indeks " + str(mid)
        elif target < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
