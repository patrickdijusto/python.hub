# count number of cars in an image using python

import cv2
print("Successfully imported cv2")

import matplotlib.pyplot as pit
print("Successfully imported matplotlib.pyplot as pit")

import cvlib as cv
print("Successfully imported cvlib as cv")

from cvlib.object_detection import draw_bbox
print("Successfully from cvlib.object_detection imported draw_bbox")

im = cv2.imread('cars_image.jpeg')
print("Successfully read cars_image")

bbox, label, conf = cvimagedetect_common_objects(im)

output_image = draw_bbox(im, bbox, label, conf)

plt.imshow(output_image)

plt.show()

print("Number of cars in the image is "+str(label.count('car')))
