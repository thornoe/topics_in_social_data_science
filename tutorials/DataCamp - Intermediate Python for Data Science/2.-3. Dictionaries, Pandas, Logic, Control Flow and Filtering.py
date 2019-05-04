# Intermediate Python for Data Science - a highly recommendable paid course #
https://www.datacamp.com/courses/intermediate-python-for-data-science

## Dictionaries, Pandas, Logic, Control Flow and Filtering ##
import pandas as pd
import numpy as np

### Import (example) ###
data = pd.read_csv("path/to/data.csv", index_col=0) # leave out "index" if not indexed

### Dictionary vs. list ###
# use a list when the order matters
# use a dictionary as a lookup table with unique keys

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
europe.keys() # Keys in europe
europe['norway'] # The value that belongs to key 'norway'
europe['denmark'] = 'copenhagen' # add or edit data point directly
del(europe['france'])

### Pandas ###
# Ex.1: Creating a DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country':names , 'drives_right':dr, 'cars_per_cap':cpc }

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)
cars.index = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']
cars.to_csv('tutorials/DataCamp - Intermediate Python for Data Science/cars.csv', index=True)

## loc
cars.loc[["RU","MOR"], ['cars_per_cap']]
cars.loc[:, ['cars_per_cap']]

## iloc
cars.iloc[[-3,-2]]

# Ex.2 drives-right countries
sel = cars[cars['drives_right']]
print(sel)

# Ex.2 car-maniac countries
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]
print(car_maniac)

### Boolean operators ###
not(False == 1) and np.sqrt(3) != 1.7
np.pi == 3.1427 or type(np.pi) == float

## Boolean operatos with NumPy
# Ex.3.a
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))

# Ex.3.b
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]
medium  # df of countries with a medium-sized car-pool
right = cars[cars['drives_right']]
right  # df of countries with right-side-driving

### Conditional statements ###
if
elif
else

# Ex. 3 if-elif-else construct for area
area = 14.0
if area > 15:
    print("big place!")
elif area > 10:
    print("medium size, nice!")
else:
    print("pretty small.")
