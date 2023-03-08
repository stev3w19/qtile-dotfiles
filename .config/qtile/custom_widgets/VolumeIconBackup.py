import re
import subprocess
from libqtile import bar
from libqtile.command.base import expose_command
from libqtile.widget import base
from libqtile import images
from libqtile.lazy import lazy

from libqtile.log_utils import logger


re_vol = re.compile(r"(\d?\d?\d?)%")

class VolIcon(base._Widget):
    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ("theme_path", "~/.config/qtile/assets", "Path of the icons"),
        (
            "get_volume_command",
            "amixer get Master",
        ),
    ]

    def __init__(self, **config):
        base._Widget.__init__(self, length=36, **config)
        self.surfaces = {}
        self.add_defaults(VolIcon.defaults)

    def _configure(self, qtile, parent_bar):
        self.length_type = bar.STATIC
        base._Widget._configure(self, qtile, parent_bar)

        self.timeout_add(0.1, self.update)
        self.setup_images()

    def update(self):
        self.volume = self.get_volume()
        self._update_drawer()
        self.bar.draw()

    def _update_drawer(self):
        self.drawer.clear(self.background or self.bar.background)
        self.drawer.clear(self.background or self.bar.background)
        if self.volume < 0:
            img_name = "audio-volume-muted"
        elif self.volume >= 80:
            img_name = "audio-volume-high"
        elif self.volume >= 40:
            img_name = "audio-volume-medium"
        elif self.volume > 0:
            img_name = "audio-volume-low"
        else:  
            img_name = "audio-volume-zero"

        self.drawer.ctx.translate(0, 5)
        self.drawer.ctx.set_source(self.surfaces[img_name])
        self.drawer.ctx.paint()

    def setup_images(self):
        names = (
            "audio-volume-high",
            "audio-volume-low",
            "audio-volume-medium",
            "audio-volume-zero",
            "audio-volume-muted",
        )
        d_images = images.Loader(self.theme_path)(*names)
        for name, img in d_images.items():
            new_height = self.bar.height - 10
            img.resize(height=new_height)
            # if img.width > self.length:
                # self.length = img.width + self.actual_padding * 2
            self.surfaces[name] = img.pattern

    def get_volume(self):
        mixer_out = subprocess.getoutput(self.get_volume_command)
        if "[off]" in mixer_out:
            return -1
        volgroups = re_vol.search(mixer_out)
        if volgroups:
            return int(volgroups.groups()[0])
        else: # error?
            return -2

    def draw(self):
        # self.drawer.draw(offsetx=self.offset, offsety=self.offsety, width=self.length)
        self.drawer.draw(offsetx=self.offset, offsety=self.offsety, width=self.length)

    @expose_command()
    def force_update(self):
        self.update()


class VolText(base._TextBox):
    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        (
            "get_volume_command",
            "amixer get Master",
            "Command to get the current volume. "
            "The expected output should include 1-3 numbers and a ``%`` sign.",
        ),
    ]

    def __init__(self, **config):
        base._TextBox.__init__(self, "VOLUME?", **config)
        self.add_defaults(VolText.defaults)
        self.length_type = bar.STATIC
        self.length = 44

    def _configure(self, qtile, bar):
        base._TextBox._configure(self, qtile, bar)
        self.timeout_add(0.1, self.update)

    def update(self):
        self.volume = self.get_volume()
        self._update_drawer()
        self.bar.draw()
        # lazy.widget["volicon"].force_update()

    def _update_drawer(self):
        if self.volume < 0:
            self.text = "mute"
        else:
            self.text = "{}%".format(self.volume)
    
    def get_volume(self):
        mixer_out = subprocess.getoutput(self.get_volume_command )
        if "[off]" in mixer_out:
            return -1
        volgroups = re_vol.search(mixer_out)
        if volgroups:
            return int(volgroups.groups()[0])
        else: # error?
            return -1

    @expose_command()
    def force_update(self):
        self.update()
