import matplotlib.pyplot as plt
import numpy as np
import skimage.io
from skimage.color import rgb2gray

clown = skimage.io.imread('http://users.accesscomm.ca/bostrum/Imaging/tips/images/FFTeg2/ClownOrig.jpg')
clown = rgb2gray(clown)
plt.subplot(141)
plt.imshow(clown)

ft = np.fft.fft2(clown)
ftshift = np.fft.fftshift(ft)
spek = 20 * np.log(np.abs(ftshift))
plt.subplot(142)
plt.imshow(spek)


def createcirclemask(center, radius):
    return (x - center[0]) ** 2 + (y - center[1]) ** 2 < radius ** 2


x, y = np.indices(clown.shape)
mask = createcirclemask((135, 126), 5)
mask2 = createcirclemask((123, 189), 10)
mask3 = createcirclemask((171, 104), 10)
mask4 = createcirclemask((159, 168), 5)

ftshift_mask = ftshift - (ftshift*mask + ftshift*mask2 + ftshift*mask3 + ftshift*mask4)
spek = 20 * np.log(np.abs(ftshift_mask))
plt.subplot(143)
plt.imshow(spek)

ftishift_back = np.fft.ifftshift(ftshift_mask)
im_back = np.fft.ifft2(ftishift_back)
im_back = np.abs(im_back)
plt.subplot(144)
plt.imshow(im_back)

plt.show()

