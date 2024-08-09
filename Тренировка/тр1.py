nums = [9, 6, 3, 5, 8, 4, 2, 7, 1]


def bubble_sort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True


bubble_sort(nums)
print(nums)
