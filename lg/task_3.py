# Сортировка выборкой выполняет больше сравнений,
# чем сортировка вставками, но выполняется немного быстрее.

def selection(sort_nums):
    for i in range(len(sort_nums)):
        index = i
        for j in range(i + 1, len(sort_nums)):
            if sort_nums[j] < sort_nums[index]:
                index = j
        sort_nums[i], sort_nums[index] = sort_nums[index], sort_nums[i]


nums = [54, 43, 3, 11, 0]

selection(nums)
print(nums)  # [0, 3, 11, 43, 54]


# быстрая сортировка:
# не требует много памяти и выполняется очень быстро
def partition(sort_nums, begin, end):
    part = begin
    for i in range(begin + 1, end + 1):
        if sort_nums[i] <= sort_nums[begin]:
            part += 1
            sort_nums[i], sort_nums[part] = sort_nums[part], sort_nums[i]
    sort_nums[part], sort_nums[begin] = sort_nums[begin], sort_nums[part]
    return part


def quick_sort(sort_nums, begin=0, end=None):
    if end is None:
        end = len(sort_nums) - 1

    def quick(sort_nums, begin, end):
        if begin >= end:
            return
        part = partition(sort_nums, begin, end)
        quick(sort_nums, begin, part - 1)
        quick(sort_nums, part + 1, end)

    return quick(sort_nums, begin, end)


quick_sort(nums)
print(nums)  # [0, 3, 11, 43, 54]
