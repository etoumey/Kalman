from mpu6050 import mpu6050
from time import sleep
import math
#Put mpu6050 in corresponding ports to first 4 pins
outFile = open('outFile.dat','w')

sensor = mpu6050(0x68)
while True:
	dataAccel = sensor.get_accel_data()
	dataGyro = sensor.get_gyro_data() 
        print "x: %s" % dataAccel['x']
        print "y: %s" % dataAccel['y']
        print "z: %s\n" % dataAccel['z']
	print "xRot: %s" % dataGyro['x']
        print "yRot: %s" % dataGyro['y']
        print "zRot: %s\n" % dataGyro['z']
	outFile.write("%s %s %s %s %s %s\n" % (dataAccel['x'], dataAccel['y'], dataAccel['z'], dataGyro['x'], dataGyro['y'], dataGyro['z']))
	

outFile.close()

