import cv2
from PIL import Image

img = cv2.imread('resources/images/fild_mine_map.png')
shape_image = img.shape
print(shape_image)

#червона сітка
#img[::30, :] = img[:, ::30] = (255, 0, 0)
#img[::30, :].putalpha(128)
#print(type(img[::30, :]))
image_grid = Image.fromarray(img)
image_grid.show()

