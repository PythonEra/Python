import numpy as np  
import matplotlib.pyplot as plt  
s1 = np.random.dirichlet((10, 5, 3), 20).transpose()  
plt.barh(range(20), s1[0])  
plt.barh(range(20), s1[1], left=s1[0], color='b')  
plt.barh(range(20), s1[2], left=s1[0]+s1[1], color='g')  
plt.title("Lengths of Strings")  
plt.show() 
