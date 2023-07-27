from PIL import Image

# Open the image
img = Image.open('path_to_image.jpg')

# Display the image
img.show()

# Get image information
print(img.format)
print(img.size)
print(img.mode)

# Convert image to numpy array
import numpy as np
img_array = np.array(img)

# Convert image to grayscale
img_gray = img.convert('L')

# Save the image
img.save('new_image.jpg')
