import numpy as np
import cv2
from matplotlib import pyplot as plt

raw = cv2.imread('../../OpenCV-3-Computer-Vision-with-Python-Cookbook/data/Lena.png')
b,g,r = cv2.split(raw)
corrected = cv2.merge([r,g,b])
lb = np.array(b*0.2, dtype='uint8')
print('b', b)
print('lb', lb)
less_blue = cv2.merge([r,g,lb])

plt.subplot(221).set_title('raw');plt.xticks([]);plt.yticks([]);plt.imshow(raw)
plt.subplot(222).set_title('corrected');plt.xticks([]);plt.yticks([]);plt.imshow(corrected)
plt.subplot(223).set_title('less blue');plt.xticks([]);plt.yticks([]);plt.imshow(less_blue)

plt.show()
