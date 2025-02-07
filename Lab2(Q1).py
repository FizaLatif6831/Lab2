import matplotlib.pyplot as plt
import numpy as np


group_A = [12, 15, 14, 13, 16, 18, 19, 15, 14, 20, 17, 14, 15,40,45,50,62]
group_B = [12, 17, 15, 13, 19, 20, 21, 18, 17, 16, 15, 14, 16, 15]

plt.boxplot(group_A)
plt.show()

plt.boxplot(group_B)
plt.show()
