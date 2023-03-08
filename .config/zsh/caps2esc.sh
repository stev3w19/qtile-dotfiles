#!/bin/zsh

devPathArr=(/dev/input/by-path/platform-i8042-serio-0-event-kbd /dev/input/by-id/usb-Ducky_Ducky_One_3_TKL_RGB_DK-V1.07-220107-if01-event-kbd)

for devpath in "${devPathArr[@]}" 
do
  if [[ -e "$devpath" ]]; then
    intercept -g $devpath | caps2esc -m 0| uinput -d $devpath &
  fi
done
