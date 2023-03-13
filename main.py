# # ==================== Getting absent numbers of list ====================

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

#   for i in range(1, len(arr)):
#     for j in range(len(arr)):
#       if arr[j] > arr[i]:
#         [arr[i], arr[j]] = [arr[j], arr[i]]
#   return arr

# print(absentNumbersOfList(some_arr))
# print(absentNumbersOfList([12,5,9,21]))


# # # ==================== Matrix sum ====================

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

# # # ==================== Adjacent Elements Product ====================

# adjacent_list = [3, 6, -2, -5, 7, 3]

# def adjacentElementsProduct(arr):
#   new_arr = []
#   max = arr[0]
#   for i in range(1, len(arr)):
#     new_arr += [arr[i - 1] * arr[i]]
#   for i in range(len(new_arr)):
#     if new_arr[i] > max:
#       max = new_arr[i]
#   return max

# print(adjacentElementsProduct(adjacent_list))

# # # ==================== Getting max number in diagonal of 2d list ====================

# matrix = [
#   [1,2,3,4,5], 
#   [6,7,8,9,10], 
#   [11,12,33,14,15],
#   [16,45,18,19,20],
#   [21,22,23,24,25]
# ]

# # -------- Left to right --------
# def getMaxNumber(arr):
#   max = arr[0][0]
#   for i in range(len(arr)):
#     if arr[i][i] > max:
#       max = arr[i][i]
#   return max

# # -------- Right to left --------

# def getMaxNumber(arr):
#   max = arr[0][-1]
#   for i in range(len(arr)):
#     if arr[i][-1 - i] > max:
#       max = arr[i][-1 - i]
#   return max

# print(getMaxNumber(matrix))

# # # ==================== Getting longest strings from list ====================

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

# # # ==================== Is lucky number ====================

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

# # # ==================== Getting sum of workers from dictionary ====================

# workers = [
#     {
#       "name": "Poghos",
#       "surname": "Poghosyan",
#       "position": "Frontend",
#       "salary": 300000
#     },
#     {
#        "name": "Martiros",
#        "surname": "Martirosyan",
#        "position": "Backend",
#        "salary": 250000
#     }
# ]

# def worker(workers):
#     sum = 0
#     for worker in workers:
#         sum += worker["salary"]
#     return str(sum) + "AMD"

# print(worker(workers))

# # # ==================== Getting factorial of number using recursion ====================

# def factorial(num):
#     if (num == 1):
#         return 1
#     return num * factorial(num - 1)
    
# print(factorial(6))

# # # ==================== Getting sum of list using recursion ====================

# def sum_of_arr(arr):
#     if len(arr) == 0:
#         return 0
#     else:
#         return arr[0] + sum_of_arr(arr[1:])
    
# print(sum_of_arr([1,2,3,4,5]))

# # # ==================== Getting prime numbers from list ====================

# numbers_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

# def factorial(arr):
#   new_arr = []
#   def is_prime(num):
#     for i in range(2, num):
#       if num % i == 0:
#         return False
#     return True
#   for i in range(len(arr)):
#     number_is_prime = is_prime(arr[i])
#     if number_is_prime:
#       new_arr += [arr[i]]
#   return new_arr

# print(factorial(numbers_list))

# # # ==================== Function return's true if numbers of list incrementing by 1, else return's false ====================

# numbers_list = [1,2,3,4,5,6,7,8,10,9]

# def increasing_sequence(arr):
#   for i in range(1, len(arr)):
#     if arr[i] - arr[i - 1] > 1:
#       return False
#   return True

# print(increasing_sequence(numbers_list))

# # # ==================== Function that makes n x n list with count ====================

# def make_2d_list(x, y):
#   arr = []
#   count = 1
#   for i in range(x):
#     arr.append([])
#     for j in range(y):
#       arr[i].append(count)
#       count += 1
#   return arr  
  
# print(make_2d_list(5, 5))

# # # ==================== Function that reverse list ====================

# items_list = [1,2,3,4,5]

# def reverse_list(arr):
#   new_arr = []
#   for i in range(len(arr) - 1, -1, -1):
#     new_arr += [arr[i]]
#   return new_arr
  
# print(reverse_list(items_list))
# print(reverse_list(['I', "love", "python", "very", "much"]))

# # # ==================== Getting flatten list with sum of numbers from 2d list ====================

# numbers_list = [6,[8, 35, 2], [8],21,[5, 6, -5 , -6],14, [1, 3, -9, 0, -1]]

# def sum_of_2d_list(arr):
#   new_arr = []
#   sum = 0
#   for i in range(len(arr)):
#     if isinstance(arr[i], list):
#       for j in range(len(arr[i])):
#         sum += arr[i][j]
#       new_arr.append(sum)
#       sum = 0
#     else:
#       new_arr.append(arr[i])
#   return new_arr
  
# print(sum_of_2d_list(numbers_list))

# # # ==================== Complete the text function ====================

# words = ["first", "succeed", "again"]
# sentence = "If at _ you don’t _, try, try _."

# def complete_the_text(words, sentence):
#   for i in range(len(words)):
#     sentence = sentence.replace("_", words[i], 1)
#   return sentence      
  
# print(complete_the_text(words, sentence))


# ==================== Sort function ====================

# numbers_list = [3,1,25,68,41,72,55,11]

# def sort(arr):
#   for i in range(1, len(arr)):
#     for j in range(len(arr)):
#       if arr[j] > arr[i]:
#         [arr[i], arr[j]] = [arr[j], arr[i]] 
#   return arr

# print(sort(numbers_list))

# ==================== Function that makes pattern ====================

# def pattern(rows, char, step):
#   for i in range(1, rows + 1, step):
#     print(char * i)
#   for j in range(rows - step, 0, -step):
#     print(char * j)
  
# print(pattern(15, "8", 2))

