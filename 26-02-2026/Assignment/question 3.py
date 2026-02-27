#Find Smallest Letter Greater Than Target.
#BRUTE
def find_smallest(letters,target):
    for ch in letters:
        if ch > target:
            return ch
    return letters[0]
letters = ['c','f','j']
target = 'c'
print(f"The smallest letter greater than {target} is: ",find_smallest(letters,target))

#OPTIMAL
def find_smallest(letters,target):
    n = len(letters)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high)//2
        if letters[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    return letters[low % n]
letters = ['c','f','j']
target = 'j'
print(f"The smallest letter greater than {target} is: ",find_smallest(letters,target))
