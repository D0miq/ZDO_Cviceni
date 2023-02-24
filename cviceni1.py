import numpy as np
import skimage
import skimage.color
import skimage.io
import skimage.exposure
import skimage.data
import matplotlib.pyplot as plt

def transform(t1, lena):
  new_img = np.zeros(lena.shape).astype(np.uint8)
  h, w, _ = new_img.shape

  for x in range(w):
    for y in range(h):
      x0, y0, _ = np.matmul(t1, np.array([x, y, 1])).astype(int)
      if 0 <= x0 < w and 0 <= y0 < h:
        new_img[y, x] = lena[y0, x0]

  plt.imshow(new_img)
  plt.show()

lena = skimage.io.imread("https://i.stack.imgur.com/3T6Gc.jpg")

t1 = np.array([[2, -0.8, -25],
          [0, 2, -256],
          [0, 0 , 1]])
transform(t1, lena)

t2 = np.array([[0.5, 0, 128],
          [0, 0.5, 128],
          [0, 0, 1]])
transform(t2, lena)