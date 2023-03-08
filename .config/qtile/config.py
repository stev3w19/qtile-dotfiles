##### Qtile RC variables
from wm_prefs import *

##### My variables
from user_prefs import *
from theme_prefs import *

##### Shell Scripts to autostart
from autostart import *

##### My keybindings
from keybinds import *

##### My groups
from groups import *

##### My layouts
from layouts import *

##### My Bar
from statusbar_panel import *

  
def file(qtile):
    lazy.spawn("thunar")

keys.extend([
    Key(
        [mod], "0",
        # lazy.spawn("thunar")
        lazy.function(file)
    )
])
