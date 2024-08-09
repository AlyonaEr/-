nums = [9, 6, 3, 5, 8, 4, 2, 7, 1]


def selection_sort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest], ls[i]


selection_sort(nums)
print(nums)
