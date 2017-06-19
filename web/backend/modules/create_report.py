from flask.ext.mysql import MySQL
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

import numpy
# считываем из текстового файла по столбцам координаты
x, y, z = numpy.loadtxt('array.txt', usecols=[0,1,2], unpack=True)

# рисуем
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(x, y, z, label='ГРАААФИИИИИИИИИК')
plt.xlabel('Широта')
plt.ylabel('Долгота')

#plt.savefig('img.png')
plt.show()