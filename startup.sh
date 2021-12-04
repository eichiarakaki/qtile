#!/bin/bash

to_execute () {
    $(pwd)/Eww/eww daemon
    picom &
    udiskie &
    $HOME/.fehbg
    dunst &
    playerctld daemon &
}

brightness () {
    current_hour=$(date +%H)

    redshift -x
    if [ $current_hour -lt 12 ]; then
        redshift -O 3000
        brightnessctl set 30%
    else
        redshift -O 5500
        brightnessctl set 100%
    fi
}

to_execute
brightness