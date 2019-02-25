#1.Sum values
def sum_values(my_dictionary):
  sum = 0
  for value in my_dictionary.values():
    sum += value
  return sum

print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

#2.Even keys
def sum_even_keys(my_dictionary):
  sum = 0
  for key in my_dictionary.keys():
    if key % 2 == 0:
      sum += my_dictionary[key]
  return sum

print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

#3.Add ten
def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] = my_dictionary[key] + 10
  return my_dictionary

print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

#4.Values that are keys
def values_that_are_keys(my_dictionary):
  value_keys = []
  for value in my_dictionary.values():
    if value in my_dictionary.keys():
      value_keys.append(value)
  return value_keys

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

#5.Largest value
def max_key(my_dictionary):
  max_value = float("-inf")
  max_key = ""
  for key in my_dictionary.keys():
    if my_dictionary[key] > max_value:
      max_value = my_dictionary[key]
      max_key = key
  return max_key

print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

#6.Word length dict
def  word_length_dictionary(words):
  word_length = {key:len(key) for key in words}
  return word_length
  
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

#7.Frequency count
def frequency_dictionary(words):
  word_freq = {}
  for word in words:
    if word in word_freq.keys():
      word_freq[word] = word_freq[word] + 1
    else:
      word_freq[word] = 1
  return word_freq

print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

#8.Unique values
def unique_values(my_dictionary):
  values_list = []
  for value in my_dictionary.values():
    if value not in values_list:
      values_list.append(value)
  return len(values_list)

print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

#9.Count first letter
def count_first_letter(names):
  first_letter = {}
  for key in names:
    if key[0] not in first_letter:
      first_letter[key[0]] = 0
    first_letter[key[0]] += len(names[key])
  return first_letter

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}