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

exec pipewire &

/home/stryder/system_scripts/battery_notify.py &
