from vjoy import vj, setJoy
import numpy as np
import time
import serial
import time

def main():
	print("vj opening", flush=True)
	vj.open()

	ser = serial.Serial("COM3", 115200)

	print("Running.") 
	while True:
		data = ser.readline().decode("utf-8").split(",")
		# print("data:", data[0][1:])
		roll = int(327.68*int(data[0][1:]))
		pitch = int(327.68*int(data[1]))
		throttle = int(327.68*int(data[2]))
		yaw = int(327.68*int(data[3]))

		## CRRCsim, SkyDive:
		joystickPosition = vj.generateJoystickPosition(wAxisX = roll, wAxisY= pitch, wSlider = throttle, wAxisZ = yaw)
		## Roll and yaw inverted:
		# joystickPosition = vj.generateJoystickPosition(wAxisX = yaw, wAxisY= pitch, wSlider = throttle, wAxisZ = roll)
		## Real drone simulator:
		# joystickPosition = vj.generateJoystickPosition(wAxisX = yaw, wAxisY= throttle, wAxisXRot = roll, wAxisZ = pitch)
		

		vj.update(joystickPosition)
		time.sleep(0.01)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        ser.close()
        sys.exit(0)
	

## 0: roll
## 1: pitch
## 2: throttle
## 3: yaw
## 4:
## 5:
print("vj closing", flush=True)
vj.close()