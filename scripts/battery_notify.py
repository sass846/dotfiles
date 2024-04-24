#!/usr/bin/env python3

import time
import subprocess
import logging

BATTERY_CAPACITY = "/sys/class/power_supply/BAT0/capacity"
PLUGGED = "/sys/class/power_supply/ACAD/online"
THRESHOLD_LOW = 20
THRESHOLD_CRITICAL = 10
THRESHOLD_HIGH = 90


def send_notification(message,urgency="--urgency=normal"):
    subprocess.Popen(['notify-send',urgency,'--icon=dialog-information','\'Battery Notification\'',message])

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

        if capacity < THRESHOLD_LOW:
            send_notification(f"{capacity}% \nBatter low!!!\nPlease plug in your charger.","--urgency=critical")
        elif capacity < THRESHOLD_CRITICAL:
            send_notification(f"{capacity}% \nBattery critical!!!\nPlease plug in your charger.","--urgency=critical")
        elif capacity > THRESHOLD_HIGH:
            send_notification(f"{capacity}% \nBattery high!!!\nPlease unplug your charger.")

        time.sleep(300)

if __name__ == "__main__":
    logging.basicConfig(filename='battery_notify.log', level=logging.ERROR)
    main()
