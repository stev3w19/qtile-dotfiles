##### qtile libs
from libqtile import layout 
from libqtile.config import Match

##### My modules
from theme_prefs import *

##### Layouts
layouts = [
    layout.MonadTall(
        margin = 10,
        border_width = 3,
        border_focus = colors[25],
    ),
]

floating_layout = layout.Floating(
    border_focus = colors[12], 
    border_width = 3,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)