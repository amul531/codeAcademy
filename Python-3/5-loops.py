#1.Divisible by 10
def divisible_by_ten(nums):
  count = 0
  for num in nums:
    if num % 10 == 0:
      count += 1
  return count

print(divisible_by_ten([20, 25, 30, 35, 40]))

#2.Greetings
def add_greetings(names):
  result = []
  for name in names:
    result.append("Hello, " + name)
  return result

print(add_greetings(["Owen", "Max", "Sophie"]))

#3.Delete starting even numbers
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst.pop(0)  #lst = lst[1:]
  return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#4.Odd indices
def odd_indices(lst):
  result = []
  for i in range(1, len(lst), 2):
    result.append(lst[i])
  return result

print(odd_indices([4, 3, 7, 10, 11, -2]))

#5.Exponents
def exponents(bases, powers):
  result = []
  for base in bases:
    for pow in powers:
      result.append(base ** pow)
  return result

print(exponents([2, 3, 4], [1, 2, 3]))

#6.Larger sum
def larger_sum(lst1, lst2):
  sum1 = 0 ; sum2 = 0
  for i in lst1:
    sum1 += i
  for j in lst2:
    sum2 += j
  if sum1 >= sum2:
    return lst1
  else:
    return lst2

print(larger_sum([1, 9, 5], [2, 3, 7]))

#7.Over 9000
def over_nine_thousand(lst):
  sum = 0; i = 0
  while (i < len(lst)) and (sum < 9000):
    sum += lst[i]
    i += 1
  return sum


print(over_nine_thousand([8000, 900, 120, 5000]))
print(over_nine_thousand([]))
print(over_nine_thousand([100, 200, 1000]))

#8.Max num
def max_num(nums):
  largest = nums[0]
  for num in nums:
    if num > largest:
      largest = num
  return largest

print(max_num([50, -10, 0, 75, 20]))

#9.Same values
def same_values(lst1, lst2):
  result = []
  for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
      result.append(i)
  return result
  

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

#10.Reversed list
def reversed_list(lst1, lst2):
  len2 = len(lst2)-1
  for i in range(len(lst1)):
    if (lst1[i] != lst2[len2-i]):
      return False;
  return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))