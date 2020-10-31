import matplotlib.pyplot as plt
import numpy as np

def normal(mu, sigma2) :
  # Add code to generate a geometric random variable here
  
expectation, variance = 3, 0.5
indices, average = np.zeros(200), np.zeros(200) 
for i in range(200) : 
  # Add code to calculate average from n normal random variables here and to thus 
  # set the elements of the list called average.  Also write code to set the elements 
  # of the list called indices. 
  
  
  
# This will plot the graph for the data
plt.plot( indices, average, 'b.' )
plt.xlabel("Number of random variables")
plt.ylabel("Sample mean")
plt.plot( [0,200], [expectation,expectation], 'r-')
plt.savefig("average_normal.png")
