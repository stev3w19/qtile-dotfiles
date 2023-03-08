#!/bin/sh

# sets keyboard layout
setxkbmap -layout gb

# sets dpi from .Xresources
userresources=$HOME/.config/X11/.Xresources
if [ -f "$userresources" ]; then
    xrdb -merge "$userresources"
fi
