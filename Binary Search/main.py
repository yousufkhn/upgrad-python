array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l = 0
r = len(array)-1
target = int(input("Enter the number u want to search"))

while (l <= r):
    middle = r+l//2
    if (array[middle] == target):
        print(middle)
        break
    elif (target < array[middle]):
        r = middle-1
    elif (target > array[middle]):
        l = middle + 1
    else:
        print("error")
