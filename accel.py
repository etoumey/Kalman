from mpu6050 import mpu6050
from time import sleep
import math

outFile = open('acceleration.dat', 'w')
outFile.write('# x y z mag\n')

sensor = mpu6050(0x68)
while True:
	dataAccel = sensor.get_accel_data()
        print "x: %s" % dataAccel['x']
        print "y: %s" % dataAccel['y']
        print "z: %s\n" % dataAccel['z']
 
        mag = math.sqrt(dataAccel['x']**2 + dataAccel['y']**2 + dataAccel['z']**2)

	if ( mag > 12)
        

	outFile.write("%s %s %s %s\n" % (dataAccel['x'], dataAccel['y'], dataAccel['z'], mag))



	sleep(1)

outFile.close()
