#1.Count letters
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):  
  count = 0
  for i in letters:
    if i in word:
      count += 1
  return count
      
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

#2.Count X
def count_char_x(word, x):
  return word.count(x)
  
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

#3.Count multi X
def count_multi_char_x(word, x):
  splits = word.split(x)
  return len(splits)-1

print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

#4.Substring between letters
def substring_between_letters(word, start, end):
  if start not in word or end not in word:
    return word
  else:
    return word[word.find(start)+1:word.find(end)]
  
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

#5.XLength
def x_length_words(sentence, x):
  for word in sentence.split():
    if len(word) < x:
      return False
  return True

print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True

#6.Check name
# Write your check_for_name function here:
def check_for_name(sentence, name):
  if name.lower() in sentence.lower():
    return True
  else:
    return False

print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

#7.Every other letter
def every_other_letter(word):
  new_word = ''
  for i in range(0, len(word), 2):
    new_word += word[i]
  return new_word

print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 

#8.Reverse
def reverse_string(word):
  rev_index = len(word)-1
  new_word = ''
  while(rev_index >= 0):
    new_word += word[rev_index]
    rev_index -= 1
  return new_word

print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

#9.Make spoonerism
def make_spoonerism(word1, word2):
  word12 = word2[0] + word1[1:]
  word21 = word1[0] + word2[1:]
  return (word12 + " " + word21)

print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

#10.Add exclamation
def add_exclamation(word):
  while (len(word) < 20):
    word += "!"
  return word

print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn