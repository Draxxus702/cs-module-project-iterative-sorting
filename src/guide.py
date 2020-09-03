# import time
# nums = [28, 97, 84, 63, 66, 29, 90, 68, 96,
#         89, 15, 67, 8, 83, 46, 58, 49, 26, 13]
# my_target = 45


# def linear_search(arr, target):
#     for i in arr:
#         if i == target:
#             return True
#     return -1


# def binary_search(arr, target):
#     start = 0
#     end = len(arr) - 1

#     while end >= start:
#         middle_index = (start + end) // 2
#         middle_value = arr[middle_index]
#         if target == middle_value:
#             return True
#         if target > middle_value:
#             start = middle_index + 1
#         if target < middle_value:
#             end = middle_index - 1
#     return False


# start = time.time()
# linear_search(nums, my_target)
# end = time.time()
# print(f"linear search array of length {len(nums)} took {end-start} seconds")


# start = time.time()
# sorted_nums = sorted(nums)
# binary_search(sorted_nums, my_target)
# end = time.time()
# print(f"binary search array of length {len(nums)} took {end-start} seconds")


adding_array = [[8, 4], [90, -1, 3], [9, 62],
                [-7, -1, -56, -6], [201], [76, 18]]


# Add up and print the sum of the all of the minimum elements of each inner array:
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
count = 0
min_list = []
for i in adding_array:
    i.sort()
    min_list.append(i[0])
for i in min_list:
    count += i

sums = 0

for i in adding_array:
    sums += min(i)
print("sums", sums)
print("count", count)
