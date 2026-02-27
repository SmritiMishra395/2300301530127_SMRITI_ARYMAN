#Find the kth missing positive number 
#BRUTE
def find_missing(arr,k):
    current = 1
    i = 0
    while k > 0:
        if i < len(arr) and arr[i] == current:
            i += 1
        else:
            k -= 1
            if k == 0:
                return current
        current += 1
arr = [2,3,4,7,11]
k = 5
print(f"The {k}th missing positive number is: ",find_missing(arr,k))


#BETTER
def find_missing(arr,k):
    for num in arr:
        if num <= k:
            k += 1
        else:
            break
    return k
arr = [2,3,4,7,11]
k = 5
print(f"The {k}th missing positive number is: ",find_missing(arr,k))

#OPTIMAL
def find_missing(arr,k):
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high)//2
        missing= arr[mid] - (mid + 1)

        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    return low + k
arr = [2,3,4,7,11]
k = 5
print(f"The {k}th missing positive number is: ",find_missing(arr,k))
