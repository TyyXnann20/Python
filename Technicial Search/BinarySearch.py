def binarySearch(item, search):
    count = 0
    low, high = 0, len(item)-1
    while low <= high:
        count += 1
        mid = (low + high) // 2
        if item[mid] == search:
            return mid, count
        elif item[mid] > search:
            high = mid - 1
        else:
            mid = low + 1

list1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
search = "E"

index, time = binarySearch(list1, search)
print(f"We need {time} times to find '{list1[index]}'")