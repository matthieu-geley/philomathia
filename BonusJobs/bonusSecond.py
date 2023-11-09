input_list = [64, 34, 12, 25, 22, 11, 90]


def bubbleSort(list):
    for i in list:
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
            # print(list)
            return list

def insertionSort(list):
    for i in range(len(list)-1):
        x = list[i]
        j = i
        while j > 0 and list[j-1] > x:
            list[j] = list[j-1]
            j -= 1
        list[j] = x
        # print(list)
        return list

def fusionSort(list):
    if len(list) > 1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        fusionSort(left)
        fusionSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                list[k] = right[j]
                j += 1
            else:
                list[k] = left[i]
                i += 1
            k += 1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
        # print(list)
        return list

def partList(list, low, high, pivot):
    i = low - 1
    for j in range(low, high):
        if list[j] <= pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i+1], list[high] = list[high], list[i+1]
    return i+1

def quickSort(list, first, last):
    if first < last:
        pivot = list[last]
        part = partList(list, first, last, pivot)
        quickSort(list, first, part-1)
        quickSort(list, part+1, last)
        # print(list)
        return list


# bubbleSort(input_list)

# insertionSort(input_list)

# fusionSort(input_list)

# quickSort(input_list, 0, len(input_list)-1)