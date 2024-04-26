#!/usr/bin/env python3

import time
import subprocess
import logging
import threading

BATTERY_CAPACITY = "/sys/class/power_supply/BAT0/capacity"
PLUGGED = "/sys/class/power_supply/ACAD/online"
THRESHOLD_LOW = 20
THRESHOLD_CRITICAL = 10
THRESHOLD_HIGH = 90
LOW_POWER_AUDIO = "/home/stryder/Music/sfx/battery_low.ogg"
CRITICAL_POWER_AUDIO = "/home/stryder/Music/sfx/battery_critical.ogg"


def send_notification(message,urgency="--urgency=normal",audio_file="/home/stryder/Music/sfx/normal.ogg"):
    subprocess.Popen(['notify-send',urgency,'--icon=dialog-information','\'Battery Notification\'',message])
    subprocess.Popen(['paplay',audio_file])

def delayed_notification(message, urgency="--urgency=normal",audio_file="/home/stryder/Music/sfx/normal.ogg", delay=900):
    send_notification(message, urgency, audio_file)
    time.sleep(delay)

def read_battery_capacity():
    try:
        with open(BATTERY_CAPACITY,"r") as file:
            capacity = int(file.read().strip())
        return capacity
    except (FileNotFoundError, PermissionError, ValueError) as e:
        logging.error(f"Error opening file {BATTERY_CAPACITY}: {e}")
        return -1

def read_ac_status():
    try:
        with open(PLUGGED,"r") as file:
            status = int(file.read().strip())
        return status
    except (FileNotFoundError, PermissionError, ValueError) as e:
        logging.error(f"Error opening file {PLUGGED}: {e}")
        return -1

def main():
    prev_ac_status = read_ac_status()

    while True:
        capacity = read_battery_capacity()
        ac_status = read_ac_status()

        if ac_status != prev_ac_status:
            if ac_status == 1:
                send_notification("Battery charging")
            else:
                send_notification("Discharging","--urgency=critical")

            prev_ac_status = ac_status

        if capacity < THRESHOLD_LOW and ac_status == 0:
            threading.Thread(target=delayed_notification, args=(f"{capacity}% \nBattery low!!!\nPlease plug in your charger.","--urgency=critical",LOW_POWER_AUDIO)).start()
        elif capacity < THRESHOLD_CRITICAL and ac_status == 0:
            threading.Thread(target=delayed_notification, args=(f"{capacity}% \nBattery critical!!!\nPlease plug in your charger.","--urgency=critical",CRITICAL_POWER_AUDIO)).start()
        if capacity > THRESHOLD_HIGH and ac_status == 1:
            threading.Thread(target=delayed_notification, args=(f"{capacity}% \nBattery high!!!\nPlease unplug your charger.", None)).start()


if __name__ == "__main__":
    logging.basicConfig(filename='battery_notify.log', level=logging.ERROR)
    main()
