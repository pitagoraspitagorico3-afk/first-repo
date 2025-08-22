from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)

if random_planet =='Mercury':
    radius = 2440
elif random_planet=='Venus':
    radius = 6052
elif random_planet=='Earth':
    radius = 6371
elif random_planet=='Mars':
    radius = 3390
elif random_planet=='Saturn':
    radius = 58232
else:
    print('Oops! Something went wrong')

area=(pi*4)*(radius**2)
print('the planet is:', random_planet,'and its area is:', area)
