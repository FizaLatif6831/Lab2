import matplotlib.pyplot as plt
import numpy as np

file = open("genome.txt","r")
data= file.read()

genome_sequence=data

genome_sequence_list=list(genome_sequence)
genome_length=len(genome_sequence)

print(genome_length)

# We want to span a range so that the helix makes a few turns.
t = np.linspace(0, 4 * np.pi, genome_length) # 4*pi gives about 2 turns
x = np.cos(t)
y = np.sin(t)
z = np.linspace(0, 5, genome_length) # z increases linearly to spread out the helix vertically
# Combine the coordinates into a (genome_length x 3) array
coordinates = np.column_stack((x, y, z))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



colors={'A':'red','T':'blue','C':'green','G':'orange'}

# for i,genome_seq in enumerate(genome):
ax.plot(coordinates[:,0],coordinates[:,1],coordinates[:,2],color = 'red',marker='o')

plt.show()