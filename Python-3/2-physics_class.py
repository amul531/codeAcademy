train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

#convert farenheit to celsius
def f_to_c(f_temp):
  return (f_temp - 32) * 5/9

f100_in_celsius = f_to_c(100)
print("%.4f" %f100_in_celsius)

#convert celsius to farenheit
def c_to_f(c_temp):
  return c_temp * (9/5) + 32

c0_in_farenheit = c_to_f(0)
print(c0_in_farenheit)

#calculating force
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print(train_force)
print("The GE train supplies {X} Newtons of force.".format(X=train_force))

#calculating energy
def get_energy(mass, c=(3*10*8)):
  return mass * c

bomb_energy = get_energy(bomb_mass)
print(bomb_energy)
print("A 1kg bomb supplies " + str(bomb_energy)  + " Joule.")

#caluclating work
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print(train_work)
print("The GE train does {X} Joules of work over {Y} meters.".format(X=train_work, Y=train_distance))
