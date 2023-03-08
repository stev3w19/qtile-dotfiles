##### Defines output in fetch
from libqtile.scripts.main import VERSION
wmname = f"Qtile {VERSION}"

##### Preferences
mod             = "mod4"
terminal        = "kitty"
launcher        = "rofi -show drun"

music_player    = "kitty -e ncmpcpp"
browser         = "librewolf"
browser_two     = "librewolf -P Work"
gui_editor      = "vscodium"
gui_file        = "thunar"

### command strings
brightness_up   = "brillo -e -q -u 100000 -A 5"
brightness_down = "brillo -e -q -u 100000 -U 5"

volume_up       = "amixer set Master unmute 5%+"
volume_down     = "amixer set Master unmute 5%-"
volume_mute     = "amixer set Master toggle"
