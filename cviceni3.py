import matplotlib.pyplot as plt
import numpy as np
import skimage.io

# Prvni ukol: vyhlazeni histogramu
# lena = skimage.io.imread("https://i.stack.imgur.com/3T6Gc.jpg")
# a, b, _ = plt.hist(lena.ravel(), 255)
# mask = np.array([1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9])
# result = np.convolve(a, mask, "same")
# plt.plot(b[:-1], result)
# plt.show()


# Druhy ukol: napsat vlastni konvoluci s Laplacovym operatorem
# def convolve(image, mask):
#     new_img = np.zeros(image.shape).astype(int)
#     h, w = image.shape
#
#     for x in range(1, w - 1):
#         for y in range(1, h - 1):
#             new_img[x, y] += image[x - 1, y - 1] * mask[0, 0]
#             new_img[x, y] += image[x, y - 1] * mask[1, 0]
#             new_img[x, y] += image[x + 1, y - 1] * mask[2, 0]
#
#             new_img[x, y] += image[x - 1, y] * mask[0, 1]
#             new_img[x, y] += image[x, y] * mask[1, 1]
#             new_img[x, y] += image[x + 1, y] * mask[2, 1]
#
#             new_img[x, y] += image[x - 1, y + 1] * mask[0, 2]
#             new_img[x, y] += image[x, y + 1] * mask[1, 2]
#             new_img[x, y] += image[x + 1, y + 1] * mask[2, 2]
#
#     return new_img
#
#
# cameraman = skimage.data.camera()
# laplace = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
# result = convolve(cameraman, laplace)
# plt.imshow(result, cmap="gray")
# plt.show()


