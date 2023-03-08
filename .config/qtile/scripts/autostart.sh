#!/bin/sh


# X11 compositor
picom &


# X11 gamma setter
killall redshift
redshift &
# X11 wallpaper set with nitrogen
nitrogen --restore


### User apps to launch
# polkit agent
lxsession &
dunst &
# Systray apps
udiskie --tray &
keepassxc &
blueman-applet &

setxkbmap -layout gb