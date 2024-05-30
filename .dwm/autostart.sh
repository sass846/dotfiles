#!/bin/sh

# Set wallpaper using feh
feh --bg-fill /home/strider/Wallpaper/Wallpaper.png &

# Start picom for compositing (transparency and shadows)
picom &

# Start slstatus
 slstatus &

# Start  dunst
dunst &

#Turn off screen blanking
xset s off -dpms

/usr/bin/pipewire &
/usr/bin/pipewire-pulse &
/usr/bin/pipewire-media-session &
# /home/strider/system_scripts/battery_notify.py &
