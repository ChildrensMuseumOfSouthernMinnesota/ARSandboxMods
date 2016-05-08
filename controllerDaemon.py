#!/usr/env python

import serial, subprocess, os, signal
from evdev import uinput, ecodes
#from pykeyboard import PyKeyboard

#k = PyKeyboard()

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

kinect_proc = ""
proc = ""
proj_proc = ""

while True:
	command = ser.readline().strip()
	if (command == "On"):
		if (proc == ""):
			proc = subprocess.Popen(["/home/cmsm/src/SARndbox-1.6/bin/SARndbox", "-fpv", "-ws 3.0 30"])
	elif (command == "Projector"):
		if (proj_proc == ""):
			proj_proc = subprocess.Popen("/home/cmsm/Desktop/CalibrateProjector")
	elif (command == "Kinect"):
		if (kinect_proc == ""):
			pointsFile = open("/home/cmsm/Desktop/points.txt", 'w')
			kinect_proc = subprocess.Popen(["/home/cmsm/Vrui-3.1/bin/RawKinectViewer", "-compress 0"], stdout=pointsFile)
			pointsFile.close()
	elif (command == "Off"):
		if (proc != ""):
			os.kill(proc.pid, signal.SIGINT)
			proc = ""
		if (kinect_proc != ""):
			os.kill(kinect_proc.pid, signal.SIGINT)
			kinect_proc = ""
		if (proj_proc != ""):
			os.kill(proj_proc.pid, signal.SIGINT)
			proj_proc = ""
	elif (command == "Shutdown"):
		if (proc != ""):
			os.kill(proc.pid, signal.SIGINT)
			proc = ""
		os.system("/usr/bin/sudo /sbin/shutdown now -h")
	
