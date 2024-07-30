import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img=mpimg.imread('./uploads/test1.jpg')
imgplot = plt.imshow(img)
plt.show()