from libqtile import hook
import os
import subprocess
from libqtile.lazy import lazy

# def multiply(qtile, value, multiplier=10):
    # logger.warning(f"Multiplication results: {value * multiplier}")
    # lazy.spawn("thunar")




##### Autostart
@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
    subprocess.Popen([script])


    
### Autoload
@hook.subscribe.startup
def autostart():
    script = os.path.expanduser('~/.config/qtile/scripts/autoload.sh') 
    subprocess.Popen([script])

    # lazy.function(multiply, 10, multiplier=2)
    # lazy.spawn("thunar")