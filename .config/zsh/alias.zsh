# core commands
alias ..='cd ..'

# core coreutils replacement
alias ls='lsd -l -A'
#alias ls='ls -lA | grep "^d" && ls -la | grep -v "^d"'

# dotfiles - git bare repo
alias dot='/usr/bin/git --git-dir=$HOME/qtile-dotfiles/ --work-tree=$HOME'

# editor
alias v='nvim'
alias sv='sudoedit'

# pacman
alias pacor='sudo pacman -Qtdq | sudo pacman -Rns -'

# grub
alias grub-update='sudo grub-mkconfig -o /boot/grub/grub.cfg'

# cli apps
alias ani='ani-cli -c'
alias dl='cd ~/Music/.spotdl/ && spotdl'
# ricing wip
alias zshc='cd ~/.config/zsh/'
alias awm='cd ~/.config/awesome'
alias wm='cd ~/.config/qtile/'

alias ki='v ~/.config/kitty/kitty.conf'
alias nv='v ~/.config/nvim/init.vim'
alias pi='v ~/.config/picom/picom.conf'

alias grubtheme='cd /usr/share/grub/themes/'
alias grubconf='sv /etc/default/grub'
alias sddmtheme='cd /usr/share/sddm/themes/'
alias sddmconf='sv /etc/sddm.conf'

alias ro='v ~/.config/rofi/config.rasi'

alias cmpd='v ~/.config/mpd/mpd.conf'
alias nc='cd ~/.config/ncmpcpp/'

alias ccd='cd ~/.config/'


