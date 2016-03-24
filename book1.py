'''
Created on Jan 12, 2015

@author: edwingsantos
'''

if __name__ == '__main__':
    pass

import numpy as np
from PIL import Image
import matplotlib.pylab as plt


i = Image.open("face.jpg")

x=  np.array(i)
#print x

print x[1][3]
    
i.show()
