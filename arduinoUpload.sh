#!/bin/bash

pkill -f controllerDaemon.py
cd ~/ARSandboxMods
pio run --target upload
python ~/ARSandboxMods/controllerDaemon.py&
