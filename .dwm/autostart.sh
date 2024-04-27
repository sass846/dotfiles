#!/bin/sh

# Set wallpaper using feh
feh --bg-fill /home/stryder/Wallpaper/Wallpaper.png &

# Start picom for compositing (transparency and shadows)
picom &

# Start slstatus
# slstatus &

# Start  dunst
dunst &

#Turn off screen blanking
xset s off -dpms

/home/stryder/scripts/battery_notify.py &
