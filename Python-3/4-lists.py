#1.Double index
def double_index(lst, index):
  if index < len(lst):
    lst[index] = lst[index] * 2
  return lst

print(double_index([3, 8, -10, 12], 2))

#2.Removing middle
def remove_middle(lst, start, end):
  lst1 = lst[0:start]
  lst2 = lst[end+1:]
  return lst1 + lst2

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#3.More than N
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  return False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

#4.More frequent item
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  return item2

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

#5.Middle item
def middle_element(lst):
  mid = int(len(lst)/2)
  if len(lst) % 2 != 0:
    return lst[mid]
  return (lst[mid] +  lst[mid - 1])/2 

print(middle_element([5, 2, -10, -4, 4, 5]))

#6.Append sum
def append_sum(lst):
  i = 1
  while i <= 3:
    lst.append(lst[-1] + lst[-2])
    i += 1
  return lst

print(append_sum([1, 1, 2]))

#7.Larger list
def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  return lst2[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

#8.Combine sort
def combine_sort(lst1, lst2):
  new_list = sorted(lst1 + lst2)
  return new_list

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

#9.Append size
def append_size(lst):
  lst.append(len(lst))
  return lst

print(append_size([23, 42, 108]))

#10.Every three nums
def every_three_nums(start):
  lst = []
  if start <= 100:
    while start <= 100:
      lst.append(start)
      start += 3
  return lst

print(every_three_nums(91))