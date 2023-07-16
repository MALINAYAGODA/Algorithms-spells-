def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (high + low) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            low = mid + 1
        else:
            high = mid - 1
    return None


print(binary_search([1, 7, 3, 4], 7))
