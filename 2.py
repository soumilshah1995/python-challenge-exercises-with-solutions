import numpy as np


class Average_Pool(object):
    def __init__(self):
        pass

    def average_pooling(self, image):

        row = image.shape[0]
        columns = image.shape[1]

        average_pool_image = np.zeros(shape=(row//2,columns//2))

        for i in range(0,row//2):

            for j in range(0,columns//2):

                average_pool_image[i,j] = (image[2*i,2*j] +
                                           image[2*i, 2*j+1] +
                                           image[2*i+1,2*j]+
                                           image[2*i+1, 2*j+1])/4.0
        return average_pool_image

x = np.random.uniform(low=-1, high=1, size=(8,8))
print(x)
print("="*66)
print("\n")
T = Average_Pool()
print(T.average_pooling(x))




