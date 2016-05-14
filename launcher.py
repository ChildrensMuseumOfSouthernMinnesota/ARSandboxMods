#!/usr/bin/env python

import subprocess, signal

controller = ""

def launch(sig, stack):
    if (controller == ""):
        controller = subprocess.Popen("python ~/ARSandboxMods/controllerDaemon.py")

def close(sig, stack):
    if (controller != ""):
        controller.kill()
        controller = ""

signal.signal(signal.SIGUSR1, launch)
signal.signal(signal.SIGUSR2, close)

while True:
    
