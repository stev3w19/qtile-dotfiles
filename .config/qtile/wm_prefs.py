##### qtile libs
from libqtile.config import Click, Drag
from libqtile.lazy import lazy

##### my modules
from user_prefs import *

##### Mouse behaviour
mouse = [
    # Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button1", lazy.window.set_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True

dgroups_key_binder = None
dgroups_app_rules = []  

auto_fullscreen = True
auto_minimize = True

reconfigure_screens = True
focus_on_window_activation = "smart"

wl_input_rules = None