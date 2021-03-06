#!/usr/env python

import serial, subprocess, os, signal
from evdev import uinput, ecodes
import pyautogui
#from pykeyboard import PyKeyboard

#k = PyKeyboard()

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

kinect_proc = ""
proc = ""
proj_proc = ""
pointsFile = ""

while True:
	command = ser.readline().strip()
	if (command == "On"):
		if (proc == ""):
			proc = subprocess.Popen(["/home/cmsm/src/SARndbox-1.6/bin/SARndbox", "-fpv", "-ws 3.0 30"])
	elif (command == "Projector"):
		if (proj_proc == ""):
			proj_proc = subprocess.Popen(["/home/cmsm/Desktop/CalibrateProjector", "-loadInputGraph", "/home/cmsm/src/SARndbox-1.6/projCalib.inputgraph"], stdin=subprocess.PIPE)
	elif (command == "Kinect"):
		if (kinect_proc == ""):
			pointsFile = open("/home/cmsm/Desktop/points.txt", 'w')
			kinect_proc = subprocess.Popen(["/home/cmsm/Vrui-3.1/bin/RawKinectViewer", "-compress 0"], stdout=pointsFile)
	elif (command == "Capture"):
		if (proj_proc != ""):
			pyautogui.press('1')
	elif (command == "ResetBG"):
		if (proj_proc != ""):
			pyautogui.press('2')
	elif (command == "Off"):
		if (proc != ""):
			proc.kill()
			proc = ""
		if (kinect_proc != ""):
			kinect_proc.kill()
			kinect_proc = ""
			pointsFile.close()
		if (proj_proc != ""):
			proj_proc.kill()
			proj_proc = ""
	elif (command == "Shutdown"):
		if (proc != ""):
			os.kill(proc.pid, signal.SIGINT)
			proc = ""
		os.system("/usr/bin/sudo /sbin/shutdown now -h")
	
