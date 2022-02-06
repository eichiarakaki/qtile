#!/bin/bash


eww=$HOME/.config/qtile/eww/eww
$eww daemon -c $HOME/.config/qtile/eww/config/bar

eww_bar() { 
    eval "$HOME/.config/qtile/eww/eww -c $HOME/.config/qtile/eww/config/bar $1" 
}
eww_dashboard() { 
    eval "$HOME/.config/qtile/eww/eww -c $HOME/.config/qtile/eww/config/dashboard $1" 
}
eww_lockscreen() { 
    eval "$HOME/.config/qtile/eww/eww -c $HOME/.config/qtile/eww/config/lockscreen $1"
}


eww_bar "open bar"
