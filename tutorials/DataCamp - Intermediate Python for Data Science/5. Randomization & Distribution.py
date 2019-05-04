# Intermediate Python for Data Science - a highly recommendable paid course #
https://www.datacamp.com/courses/intermediate-python-for-data-science

# Import numpy, pyplot and set seed
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

np.random.rand() # Create a random float in [0,1]

######################################################################################
# Use randint() to simulate a dice in order to move around the empire state building #
######################################################################################
all_walks = []

# Simulate random walk 100 times
for i in range(100) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2: # go 1 step down if possible
            step = max(0, step - 1)
        elif dice <= 5: # go 1 step up
            step = step + 1
        else: # throw the dice again and go up that amount of steps
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 : # 0.1% risk of being sent home to start
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot all_walks
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()
plt.clf()

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends,bins=15)
plt.show()

# The fraction of simulations that ended higher than step 60
np.mean(ends > 60)
