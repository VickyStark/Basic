#import Pillow package
from PIL import Image

img=Image.open(#Enter your Image Name)

areas=(#Enter Your  Coordinates)
cropped_img=img.crop(areas)
print(img.size)
img.show()
cropped_img.show()
