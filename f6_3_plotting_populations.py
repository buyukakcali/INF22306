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

print('#------------------------------------------------------------------------------ Assignment 1')
plt.show()

print('#------------------------------------------------------------------------------ Assignment 2')

print(f'Assignment 2: which year each species had the largest population\n\
Carrot= {year[np.argmax(carrot_pop)]}\nHare= {year[np.argmax(hare_pop)]}\nLynx= {year[np.argmax(lynx_pop)]}')

print('#------------------------------------------------------------------------------ Assignment 3')
print(f'Assignment 3: which species has the largest population for each year\nYear = Specie')

year_max_species = []
for i in range(len(year)):
    specie = np.argmax([carrot_pop[i], hare_pop[i], lynx_pop[i]])
    if specie == 0:
        year_max_species += ['carrot']
    elif specie == 1:
        year_max_species += ['hare']
    elif specie == 2:
        year_max_species += ['lynx']

for i in range(len(year_max_species)):
    print(f'{year[i]} = {year_max_species[i]}')

print('#------------------------------------------------------------------------------ Assignment 4')

print(f'Assignment 4:  which years any of the populations is above 50,000\nYear  =  Species')

for i in range(len(year)):
    above_fifty000 = []
    if np.any(carrot_pop[i] > 50000):
        above_fifty000 += ['carrot']
    if np.any(hare_pop[i] > 50000):
        above_fifty000 += ['hare']
    if np.any(lynx_pop[i] > 50000):
        above_fifty000 += ['lynx']
    if above_fifty000 != []:
        text = ''
        for j in range(len(above_fifty000)):
            if j == len(above_fifty000)-1:
                text += above_fifty000[j]
            else:
                text += above_fifty000[j] + ', '
        print(str(year[i]) + ' = ' + text)
    else:
        print(f'{year[i]} all species are under 50.000 population')

print('#------------------------------------------------------------------------------ Assignment 5')

hare_pop_dec = np.gradient(hare_pop)

plt.figure(figsize=(8, 4))  # it defines size of figure on your screen.

plt.xlabel('Year')
plt.ylabel('Amount')
plt.title('Relation between lynx population and the hare death rate')

plt.plot(year_points, -hare_pop_dec, color='green', label='hares death rate')
plt.plot(year_points, lynx_points, color='r', label='lynxes population')

plt.xticks(np.linspace(min(year), max(year), num=5))
plt.legend()
plt.show()


hare_pop_dec = np.gradient(hare_pop)

plt.figure(figsize=(8, 4))  # it defines size of figure on your screen.

plt.xlabel('Lynxes')
plt.ylabel('Hare birth rate')
plt.title('the change in hare population against the lynx population')

plt.scatter(lynx_points, hare_pop_dec)
plt.show()

print('#------------------------------------------------------------------------------ Assignment 6')

res = np.corrcoef(hare_points, lynx_points)
print(res)