#!/bin/bash


# Processes
picom               &
udiskie             &
$HOME/.fehbg        &
dunst               &
xset r rate 300 100 & # only for x11



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
    "7")                   redshift -O 4500 &;;
    "8")                   redshift -O 4600 &;;
    "9" | "10" | "11")     redshift -O 4700 &;;
    "15" | "16" | "17")    redshift -O 4600 &;;
    "18")                  redshift -O 4500 &;;
    "19")                  redshift -O 4400 &;;
    "20")                  redshift -O 4300 &;;
    "21")                  redshift -O 4200 &;;
    "22" | "23")           redshift -O 4100 &;; 
    *);;
esac
