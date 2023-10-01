# some varialbles
logi_mouse_sensi = -0.6 # needs to me between -1 and 1

#########

import os


def ls_system():
    os.system("ls")

def is_screen_connected(ID):
    stream = os.popen(f'xrandr | grep {ID}')
    output = stream.read()
    return " connected" in output

def is_usb_connected(name):
    stream = os.popen(f'lsusb | grep "{name}"')
    output = stream.read()
    s = name in output
    if s: print(f"{name}: connected")
    else: print(f"{name}: not connected")
    return s

def run_app(app):
    stream = os.popen(f"pgrep {app}")
    output = stream.read()
    s = len(output)>1
    if s: print(f"{app}: already running")
    else:
        os.system(f"{app} &")
        print(f"{app}: now set to run")


# check screen connection
if is_screen_connected("HDMI-0") and is_screen_connected("DP-0"):
    os.system("xrandr --output DP-0 --right-of HDMI-0")
    print("Dual monitor: DP-0 set to the right of HDMI-0")

if is_screen_connected("HDMI-0"):
    os.system("xrandr --output HDMI-0 --mode 1920x1080 --rate 74")
    print("HDMI-0: resolution and rate set")
else: print("HDMI-0: not connected")

if is_screen_connected("DP-0"):
    os.system("xrandr --output DP-0 --mode 2560x1080 --rate 200")
    print("DP-0: resolution and rate set")
else: print("DP-0: not connected")


# special case for Logitech mouse
mouse_status = False
if is_usb_connected("Logitech, Inc. USB Receiver"):
    os.system(f'xinput --set-prop "Logitech USB Receiver" "libinput Accel Speed" {logi_mouse_sensi}')
    mouse_status = True
if is_usb_connected("Logitech, Inc. PRO X Wireless"):
    os.system(f'xinput --set-prop "Logitech PRO X Wireless" "libinput Accel Speed" {logi_mouse_sensi}')
    mouse_status = True

if mouse_status:
    print(f"Logitech mouse sensivity set to {logi_mouse_sensi}")



run_app("redshift-gtk")
run_app("autotiling")
