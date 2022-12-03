#!/bin/bash


script_dir=$(cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)
# Processes
picom                  &
udiskie                &
$HOME/.fehbg           &
dunst                  &
xset r rate 300 100    & # only for x11
$script_dir/batnotify  &


# brightnessctl
current_hour=$(date +%H)
redshift -x
if [ $current_hour -lt 12 ]; then
    redshift -O 3000
    brightnessctl set 30%
else
    redshift -O 5500
    brightnessctl set 100%
fi



# redshift
if pgrep redshift > /dev/null
then
    redshift_pid=$(pidof redshift)
    kill $redshift_pid
fi

date=$(date +%H)
if [ ${date:0:1} -eq "0" ]; then
 date=${date:1:2}
fi

case $date in
    "0" | "1" | "2" | "3") redshift -O 4100 &;;
    "4")                   redshift -O 4200 &;;
    "5")                   redshift -O 4300 &;;
    "6")                   redshift -O 4400 &;;
    "21")                  redshift -O 4200 &;;
    "22" | "23")           redshift -O 4100 &;; 
    *);;
esac
