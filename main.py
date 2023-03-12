# ==================== Getting absent numbers of list ====================

# some_arr = [3,1,5,8,10]

# def absentNumbersOfList(arr):
#   min = arr[0]
#   max = arr[0]
#   for i in range(len(arr)):
#     if arr[i] > max:
#       max = arr[i]
#     if arr[i] < min:
#       min = arr[i]

#   def indexOf(arr, item):
#     for i in range(len(arr)):
#       if arr[i] == item:
#         return i
#     return -1

#   while min < max:
#     if indexOf(arr, min) == -1:
#       arr += [min]
#     min += 1

#   i = 1
#   j = 0
#   for i in range(len(arr)):
#     for j in range(len(arr)):
#       if arr[j] > arr[i]:
#         [arr[i], arr[j]] = [arr[j], arr[i]]
#   return arr

# print(absentNumbersOfList(some_arr))
# print(absentNumbersOfList([12,5,9,21]))


# ==================== Matrix sum ====================

# matrix = [
#   [1, 1, 1, 0], 
#   [0, 5, 0, 1], 
#   [2, 1, 3, 10]
# ]

# def matrixSum(arr):
#   sum = 0
#   for i in range(len(arr)):
#     for j in range(len(arr[i])):
#       if arr[i][j] == 0:
#         if i + 1 < len(arr):
#           arr[i + 1][j] = 0
#       else:
#         sum += arr[i][j]
#   return sum

# print(matrixSum(matrix))

# ==================== Adjacent Elements Product ====================

# adjacent_list = [3, 6, -2, -5, 7, 3]

# def adjacentElementsProduct(arr):
#   new_arr = []
#   max = arr[0]
#   i = 1
#   for i in range(len(arr)):
#     new_arr += [arr[i - 1] * arr[i]]
#   for i in range(len(new_arr)):
#     if new_arr[i] > max:
#       max = new_arr[i]
#   return max

# print(adjacentElementsProduct(adjacent_list))

# ==================== Getting max number in diagonal of 2d list ====================

# matrix = [
#   [1,2,3,4,5], 
#   [6,7,8,9,10], 
#   [11,12,33,14,15],
#   [16,45,18,19,20],
#   [21,22,23,24,25]
# ]

# -------- Left to right --------
# def getMaxNumber(arr):
#   max = arr[0][0]
#   for i in range(len(arr)):
#     if arr[i][i] > max:
#       max = arr[i][i]
#   return max

# -------- Right to left --------

# def getMaxNumber(arr):
#   max = arr[0][-1]
#   for i in range(len(arr)):
#     if arr[i][-1 - i] > max:
#       max = arr[i][-1 - i]
#   return max

# print(getMaxNumber(matrix))

# ==================== Getting longest strings from list ====================

# strings_list = ["bba", "vcdddd", "zjoq", "vcffdd", "vcddzz", "vcddww", "aba"]

# def longestStrings(arr):
#   max = arr[0]
#   new_arr = []
#   length = 0
#   for i in range(len(arr)):
#     if len(arr[i]) > len(max):
#       max = arr[i]
#       length = len(max)
#   for i in range(len(arr)):
#     if len(arr[i]) == length:
#       new_arr += [arr[i]]
#   return new_arr

# print(longestStrings(strings_list))

# ==================== Is lucky number ====================

# def isLucky(num):
#   first_half = 0
#   second_half = 0
#   stringify_num = str(num)
#   for i in range(int(len(stringify_num) / 2)):
#     first_half += int(stringify_num[i])
#   i = int(len(stringify_num) / 2)
#   while i < len(stringify_num):
#     second_half += int(stringify_num[i])
#     i += 1
#   return first_half == second_half

# print(isLucky(1230))