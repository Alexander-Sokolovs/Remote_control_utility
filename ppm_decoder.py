import RPi.GPIO as GPIO
import time
import serial

GPIO.setmode(GPIO.BCM)
GPIO_IN = 18
GPIO.setup(GPIO_IN, GPIO.IN)

ser = serial.Serial("/dev/ttyAMA0", 115200)

def state_0():
	while GPIO.input(GPIO_IN) == 1:
		pass
		#print("waiting...")
		#print(GPIO.input(GPIO_IN))

def state_1():
	while GPIO.input(GPIO_IN) == 0:
		pass
#		print("low...")
		#print(GPIO.input(GPIO_IN))
def state_2():
	start_time = time.time()
	stop_time = time.time()
	time_elapsed = 0
	while GPIO.input(GPIO_IN) == 1:
		pass
		#print("high")
		#print(GPIO.input(GPIO_IN))
	stop_time = time.time()
	time_elapsed = stop_time-start_time
#	if time_elapsed > 0.011:
#		print("####")
#	print(time_elapsed)
	return time_elapsed

state_0()
#msg = 'heja'
#ser.write(bytes(msg, 'utf-8'))
pr_bool = False
print("Running ppm decoder")
while True:
	vals = []
	for x in range(7):
		state_1()
		vals.append(int((state_2()*100000-60)))
		#vals.append(round(state_2(), 4))
	if pr_bool:
#		print(vals[1:])
		ser.write(bytes(str(vals[1:]), 'utf-8'))
		ser.write(bytes(b'\n'))
	pr_bool = not pr_bool
#	ser.write(bytes(b'53'))
	time.sleep(0.01)
#	print(vals[1:])
