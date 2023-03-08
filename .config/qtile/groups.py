##### qtile libs
from libqtile.config import Group, ScratchPad, DropDown, Key
from libqtile.lazy import lazy

##### My modules
### modkey variable 
from user_prefs import *
### keybinds 
from keybinds import *

##### Groups
groups = [
    Group("1", label = ""),
    Group("2", label = "󰈹"), 
    Group("3", label = "󰟪"),
    Group("4", label = "󰝚"),
    Group("5", label = "󰳰"),
]

for i in groups:
    keys.extend([
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ])

##### ScratchPad hidden group
groups.extend([
    ScratchPad("hidden", [
        DropDown("term", terminal, 
            opacity = 1.0, 
            width   = 0.8,
            height  = 0.8,
            on_focus_lost_hide = False,
        ),
        DropDown("music", music_player, 
            opacity = 1.0, 
            width   = 0.9,
            height  = 0.9,
            x = 0.05,
            y = 0.05,
            on_focus_lost_hide = False,
        ),
    ],
        None,
        "",
        True
    ),
])