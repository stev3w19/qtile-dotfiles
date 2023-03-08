#!/bin/sh
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi

~/.config/zsh/caps2esc.sh
