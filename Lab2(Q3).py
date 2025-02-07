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