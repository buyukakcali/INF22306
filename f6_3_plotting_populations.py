import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray

data = []
year = []
lynx_pop = []
hare_pop = []
carrot_pop = []

with open('populations.txt', 'r') as file:
    next(file)
    lines = file.readlines()

for i in range(len(lines)):
    line = lines[i].strip().split()
    data += [int(line[0]), int(line[1]), int(line[2]), int(line[3])]
    year += [int(line[0])]
    hare_pop += [int(line[1])] #hare_pop += [[int(line[0]), int(line[1])]]
    lynx_pop += [int(line[2])] #lynx_pop += [[int(line[0]), int(line[2])]]
    carrot_pop += [int(line[3])] #carrot_pop += [[int(line[0]), int(line[3])]]

# converting arrays to numpy array
year_points: ndarray = np.array(year)
hare_points = np.array(hare_pop)
lynx_points = np.array(lynx_pop)
carrot_points = np.array(carrot_pop)

coolor = (["blue", "red", "green"])
plt.figure(figsize=(8, 4))  # it defines size of figure on your screen.
#plt.plot(year_points, hare_points, year_points,lynx_points, year_points, carrot_points, colors=coolor) # does not work
#plt.plot(year_points, hare_points, year_points,lynx_points, year_points, carrot_points) # this code also plots but I couldn't find to add colors one by one
plt.plot(year_points, hare_points, color='b', label='hares population')
plt.plot(year_points,lynx_points, color="red", label='lynxes population')
plt.plot(year_points, carrot_points, color="green", label='carrots population')

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('population of hares, lynxes and carrots')

# first usage of xticks and np.linespace
ax = np.linspace(min(year), max(year), num=5)
plt.xticks(ax)

# second usage of xticks and np.linespace
#plt.xticks(np.linspace(min(year), max(year), num=5))

# there is no usage of 'xticks and np.linespace' at here but works like others
#plt.xticks(np.arange(min(year), max(year)+1, 5))

plt.legend() # this function writes the names and pipes with their colors on the top-right of figure

#------------------------------------------------------------------------------Assignment 1
#plt.show()

#------------------------------------------------------------------------------Assignment 2
'''
print(f'Assignment 2: which year each species had the largest population\n\
Hare= {year[np.argmax(hare_pop)]}\nLynx= {year[np.argmax(lynx_pop)]}\nCarrot= {year[np.argmax(carrot_pop)]}')

#------------------------------------------------------------------------------ Assignment 3
print(f'Assignment 3: which species has the largest population for each year\nYear = Specie')

year_max_species = []
for i in range(len(year)):
    specie = np.argmax([hare_pop[i], lynx_pop[i], carrot_pop[i]])
    if specie == 0:
        year_max_species += ['hare']
    elif specie == 1:
        year_max_species += ['lynx']
    elif specie == 2:
        year_max_species += ['carrot']

for i in range(len(year_max_species)):
    print(f'{year[i]} = {year_max_species[i]}')'''

#------------------------------------------------------------------------------ Assignment 4

print(f'Assignment 4:  which years any of the populations is above 50,000\nYear  =  Species')

above_fifty000 = []
for i in range(len(year)):
    if np.any(hare_pop[i] > 50000):
        print(f'At the end of {year[i]}, hare is over 50.000')
    if np.any(lynx_pop[i] > 50000):
        print(f'At the end of {year[i]}, lynx is over 50.000')
    if np.any(carrot_pop[i] > 50000):
        print(f'At the end of {year[i]}, carrot is over 50.000')

#--------------------------------------------------------------
print(hare_points)
print(lynx_points)
print(np.gradient(hare_points,lynx_points))