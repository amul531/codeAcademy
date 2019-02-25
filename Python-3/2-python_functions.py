#1.Average
def average(num1 ,num2):
  return (num1 + num2)/2

print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

#2.Tenth_power
def tenth_power(num):
  return num ** 10

print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

#3.Bond - introduction
def introduction(first_name, last_name):
	return "{ln}, {fn} {ln}".format(fn=first_name, ln=last_name)

print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

#4.Square root
def square_root(num):
  return num ** 0.5

print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

#5.Calculating tip
def tip(total, percentage):
  return total * (percentage/100)

print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

#6.Win percentage
def win_percentage(wins, losses):
  return (wins/(wins+losses)) * 100

print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100

#7.First three multiples
def first_three_multiples(num):
  i = 1
  while i <= 3:
    print(num * i)
    i += 1
  return num * i

first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0

#8.Dog years
def dog_years(name, age):
  age *= 7
  return "{name}, you are {age} years old in dog years".format(name=name, age=age)

print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

#9.Remainder
def remainder(num1, num2):
  return (2 * num1) % (num2 / 2)

print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0

#10.Basic math
def lots_of_math(a, b, c, d):
  add = a + b
  sub = c - d
  mul = add * sub
  print(add)
  print(sub)
  print(mul)
  return mul % a
  
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0

