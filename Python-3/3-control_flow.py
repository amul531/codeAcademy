#1.In range
def in_range(num, lower, upper):
  if num >= lower and num <=upper:
    return True
  else:
    return False

print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False

#2.Movie review
def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif 5 < rating < 9:
    return "This one was fun."
  else:
    return "Outstanding!"

print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."

#3.Twice as large
def twice_as_large(num1, num2):
  if num1 > num2 * 2:
    return True
  else:
    return False

print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True

#4.Power
def large_power(base, exponent):
  if base ** exponent > 5000:
    return True
  else:
    return False

print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False

#5.Divisible by 10
def divisible_by_ten(num):
  if num % 10 == 0:
    return True 
  else:
    return False

print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False

#6.Max number
def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"

print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"

#7.Over budget
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if budget < (food_bill + electricity_bill + internet_bill + rent):
    return True
  else:
    return False

print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True

#8.Always false
def always_false(num):
  if (num > 0 and num < 0):
    return True
  else:
    return False

print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False

#9.Not equal
def not_sum_to_ten(num1, num2):
    if num1 + num2 != 10:
      return True
    else:
      return False

print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5,5))
# should print False

#10.Same name 
def same_name(your_name, my_name):
  if your_name == my_name:
    return True
  else:
    return False

print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False