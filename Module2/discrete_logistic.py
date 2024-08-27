import numpy as np
import matplotlib.pyplot as plt 


r = 2.5
K = 0.6


starting_population = 0.3

num_days = 100



# print(population)

R_values = np.linspace(0, 3, 500)

for r in R_values:

    population = [0] * num_days
    population[0] = starting_population

    for i in range(1, num_days):
        population[i] = population[i-1] + (r * (1 - (population[i-1] / K)) * population[i-1])

    plt.scatter([r] * (num_days//2), population[num_days//2:])
    plt.xlabel('R values')
    plt.ylabel('Steady state population values')
  
plt.show()

# make different plots of r between 0 and 3 depicting either the state state or N-cycle 


    

