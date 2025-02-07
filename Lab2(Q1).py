import matplotlib.pyplot as plt
import numpy as np


group_A = [12, 15, 14, 13, 16, 18, 19, 15, 14, 20, 17, 14, 15,40,45,50,62]
group_B = [12, 17, 15, 13, 19, 20, 21, 18, 17, 16, 15, 14, 16, 15]

plt.boxplot(group_A)
plt.show()

plt.boxplot(group_B)
plt.show()



#-----------------------
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



#------------------------
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image_path = "pic.png" 
img = Image.open(image_path)


img_array = np.array(img)



plt.imshow(img_array)
plt.axis('off')
plt.show()


rotated_img = np.rot90(img_array)


plt.imshow(rotated_img)
plt.axis('off')
plt.show()

flipped_img = np.fliplr(img_array)


plt.imshow(flipped_img)
plt.axis('off')
plt.show()

if img_array.shape[2] == 4:
    img_array = img_array[:, :, :3] 


gray_img = np.dot(img_array[..., :3], [0.299, 0.587, 0.114])


plt.imshow(gray_img, cmap='gray')
plt.axis('off')
plt.show()
