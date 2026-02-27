#Floor in a sorted array
#BRUTE
def floor(nums,x):
    n= len(nums)
    floor = -1
    for i in range(0,n):
        if nums[i] <= x:
            floor = i
        else:
            break
    return floor

nums= [1, 2, 4, 6, 10]
x= 5
print(f"The floor of {x} is: ",floor(nums,x))

#OPTIMAL
def floor(nums,x):
    n = len(nums)
    floor = -1
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] <= x:
            floor = mid
            low = mid + 1
        else:
            high = mid - 1
    return floor

nums= [1, 2, 4, 6, 10]
x= 5
print(f"The floor of {x} is: ",floor(nums,x))