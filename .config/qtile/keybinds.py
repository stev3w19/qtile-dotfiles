##### qtile libs
from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.log_utils import logger

##### my modules 
from user_prefs import *

from custom_widgets.VolumeIcon import *

##### Keybinds
keys = [
    # Core binds
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key(
        [mod, "control"], "h", 
        lazy.layout.grow_left(), 
        lazy.layout.shrink_main().when(layout="monadtall"),
        desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", 
        lazy.layout.grow_right(), 
        lazy.layout.grow_main().when(layout="monadtall"),
        desc="Grow window to the right"),
    Key(
        [mod, "control"], "j", 
        lazy.layout.grow_down(), 
        lazy.layout.grow().when(layout="monadtall"),
        desc="Grow window down"),
    Key(
        [mod, "control"], "k", 
        lazy.layout.grow_up(), 
        lazy.layout.shrink().when(layout="monadtall"),
        desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Other window actions
    Key([mod], "f", lazy.window.toggle_maximize(), desc="Maximise"),
    # Workspaces
    Key([mod], "Tab", lazy.screen.toggle_group(), desc="Previous workspace"),

    # Launch apps
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key(["mod1"], "Space", lazy.spawn(launcher), desc="App Launcher"),
    Key([mod, "shift"], "m", lazy.spawn(music_player), desc="Music Player"),
    Key([mod], "i", lazy.spawn(browser), desc="Browser"),
    Key([mod, "shift"], "i", lazy.spawn(browser_two), desc="Browser alt"),
    Key([mod], "u", lazy.spawn(gui_editor), desc="GUI Editor"),
    Key([mod], "e", lazy.spawn(gui_file), desc="GUI File Manager"),

    # Media keys  
    Key(
        [], "XF86AudioMute", 
        lazy.spawn(volume_mute), 
        lazy.widget["volicon"].force_update(),
        lazy.widget["voltext"].force_update(), 
    ),
    Key(
        [], "XF86AudioRaiseVolume", 
        lazy.spawn(volume_up), 
        lazy.widget["voltext"].force_update(), 
        lazy.widget["volicon"].force_update()
    ),
    Key(
        [], "XF86AudioLowerVolume", 
        lazy.spawn(volume_down), 
        lazy.widget["voltext"].force_update(), 
        lazy.widget["volicon"].force_update()
    ),

    Key(
        [], "XF86MonBrightnessUp", 
        lazy.spawn(brightness_up),
        lazy.widget["briicon"].force_update(),
        lazy.widget["britext"].force_update(),
    ),
    Key(
        [], "XF86MonBrightnessDown", 
        lazy.spawn(brightness_down),
        lazy.widget["briicon"].force_update(),
        lazy.widget["britext"].force_update(),
    ),
        

    # ScratchPad
    Key([mod], "n", lazy.group['hidden'].dropdown_toggle('term')),
    Key([mod], "m", lazy.group['hidden'].dropdown_toggle('music')),
]




