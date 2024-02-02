#!/bin/sh

# Get battery status using acpi
battery_status=$(acpi -b | awk '{print $3}' | tr -d ',')

# Set notification thresholds
low_threshold="25"
critical_threshold="10"
full_threshold="100"

# Determine urgency level based on battery status
urgency="normal"
if [ "$battery_status" -le "$critical_threshold" ]; then
    urgency="critical"
elif [ "$battery_status" -le "$low_threshold" ]; then
    urgency="low"
fi

# Show notification using dunst
dunstify -u "$urgency" -r 1234 -p -t 0 "Battery Status" "Level: ${battery_status}%"


