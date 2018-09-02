from mpu6050 import mpu6050
from time import sleep
import math
#Put mpu6050 in corresponding ports to first 4 pins

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

	sleep(1)

