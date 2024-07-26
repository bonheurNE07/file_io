import sys
from PIL import Image

# Create an empty list to hold images
images = []

# Open each image file passed as a command-line argument and add to the list
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

# Save the images as a GIF
images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
