from mpu6050 import mpu6050
from time import sleep
import math
import numpy as np


#Put mpu6050 in corresponding ports to first 4 pins
outFile = open('outFile.dat','w')
sensor = mpu6050(0x68)

n = 10000
sz = (n, 1)

xhat = np.zeros(sz)
P = np.zeros(sz)
xhatminus = np.zeros(sz)
Pminus = np.zeros(sz)
K = np.zeros(sz)
xAccMea = np.zeros(sz)

R = .1

xhat[0] = 0.0
P[0] = 1.0

for x in range(1,n):
	dataAccel = sensor.get_accel_data()
	xAccMea[x] = dataAccel['x']
	K[x] = P[x-1]/(P[x-1]+R)
	xhat[x] = xhat[x-1]+K[x]*(xAccMea[x] - xhat[x-1])
	P[x] = (1-K[x])*P[x-1]
	outFile.write("%f %f %f\n" % (xAccMea[x], xhat[x], K[x]))
outFile.close()

