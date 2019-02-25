#a cost calculating function ->common for all shipping methods
def get_cost(weight, ship_cost, flat_charge):
  return weight * ship_cost + flat_charge

#normal ground shipping cost calculation
def normal_gs_cost(weight):
  if weight <= 2:
    cost = 1.50
  elif weight > 2 and weight <= 6:
    cost = 3.00
  elif weight > 6 and weight <= 10:
    cost = 4.00
  else:
    cost = 4.75
  return get_cost(weight, cost, 20)
    
#print(normal_gs_cost(8.4))

#premium ground shipping cost - flat rate
premium_gs_cost = 125.00

#drone shipping cost calculation
def drone_ship_cost(weight):
  if weight <= 2:
    cost = 4.50
  elif weight > 2 and weight <= 6:
    cost = 9.00
  elif weight > 6 and weight <= 10:
    cost = 12.00
  else:
    cost = 14.25
  return get_cost(weight, cost, 0)

#print(drone_ship_cost(1.5))

#cheapest shipping option calculation
def cheapest_shipping(weight):
  ground = normal_gs_cost(weight)
  drone = drone_ship_cost(weight)
  premium = premium_gs_cost
  if ground <= drone and ground <= premium:
    method = "normal ground shipping"
    cost=ground
  elif drone <= premium:
    method = "drone shipping"
    cost=drone
  else:
    method = "Premium ground shipping"
    cost=premium
  print ("The cheapest available option is %s which costs $%.2f" %(method,cost))
  
  
cheapest_shipping(17) 
cheapest_shipping(4.8) 
cheapest_shipping(41.5)