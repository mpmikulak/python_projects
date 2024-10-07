# Calculate pi to any preceision you want! (kinda)!
# Implements the Gregory-Leibniz series, the Nilakantha series, and the sine method.

import math

# Let's calculate pi using the Gregory-Leibniz series
def g_l_pi(iterations):
  pi = 0
  def odd_number(num):
    return (num * 2 + 1)
  
  for i in range(int(iterations)):
      if i % 2 == 0:
        pi += 4 / odd_number(i)
      else:
        pi -= 4 / odd_number(i)
  
  return pi
  
# Let's calculate pi using the Nilakantha series.
def nilakantha(iterations):
  fraction = 0
  denominator = 2
  for i in range(int(iterations)):
    # print(denominator)
    if i % 2 == 0:
      fraction += 4 / ((denominator) * (denominator+1) * (denominator+2))
      denominator += 2
    else:
      fraction -= 4 / ((denominator) * (denominator+1) * (denominator+2))
      denominator += 2
  return(3 + fraction)

# Let's calculate pi using a limit and the sine function.
def sine_to_pi(limit):
  return float(limit) * (math.sin(math.radians(180/int(limit))))

def calculate_pi(precision, algorithm):
  if algorithm == "1":
    return g_l_pi(precision)
  elif algorithm == "2":
    return nilakantha(precision)
  elif algorithm == "3":
    return sine_to_pi(precision)
  else:
    return "Please enter a valid algorithm."

while True:
  # Which series do you want to use?
  print("Which algorithm do you want to use?")
  print("(1) for Gregory-Leibniz series")
  print("(2) for Nilakantha series")
  print("(3) for sine")
  print("Anything else to quit")
  algorithm = input()

  # Check for non-options
  if not algorithm.isnumeric() or int(algorithm) > 3:
    print("Quiting...")
    break
  # How many iterations do you want to use?
  precision = input("To what precision do you want to calculate pi? (1 - 1,000,000)\n")
  
  # Check for invalid or out-of range inputs
  if not precision.isnumeric() or int(precision) > 1000000 or int(precision) < 1:
    print("Please enter a valid number, and nothing else.")
    break
  # Make some numbers
  print(calculate_pi(precision, algorithm))
  

