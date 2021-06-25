from PIL import Image
import glob

import numpy as np
from cv2 import imread, imwrite
for name in glob.glob('*.tif'):
    im = Image.open(name)
    name = str(name).rstrip(".tif")
    im.save(name + '.tiff', 'PNG')

for name in glob.glob('*.tiff'):
    im=imread(name,1)
    print(im.shape[0])
    im = im.reshape( im.shape[0], im.shape[1], 3)
    name = str(name).rstrip(".tiff")

    imwrite(name+".png",im)
print("Conversion from tif/tiff to png completed!")
