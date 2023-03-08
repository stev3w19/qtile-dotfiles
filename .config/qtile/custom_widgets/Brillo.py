import re
import subprocess
from libqtile import bar
from libqtile.command.base import expose_command
from libqtile.widget import base
from libqtile import images
from libqtile.lazy import lazy

from libqtile.log_utils import logger



class BriIcon(base._Widget):
    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ("padding", 3, "Padding left and right. Calculated if None."),
        ("theme_path", "~/.config/qtile/assets", "Path of the icons"),
        (
            "get_brightness_command",
            "brillo",
            "Command to get the current brightness. "
        ),
    ]

    def __init__(self, **config):
        base._Widget.__init__(self, length=32, **config)
        self.add_defaults(BriIcon.defaults)
        self.surfaces = {}

    def _configure(self, qtile, parent_bar):
        self.length_type = bar.STATIC
        base._Widget._configure(self, qtile, parent_bar)

        self.timeout_add(0, self.update)
        self.setup_images()

    def update(self):
        self.brightness = self.get_brightness()
        self._update_drawer()
        self.bar.draw()

    def _update_drawer(self):
        self.drawer.clear(self.background or self.bar.background)
        if self.brightness <= 1:
            img_name = "display-brightness-off"
        elif self.brightness <= 40:
            img_name = "display-brightness-low"
        elif self.brightness < 80:
            img_name = "display-brightness-medium"
        else:  
            img_name = "display-brightness-high"

        self.drawer.ctx.translate(0, 10)
        self.drawer.ctx.set_source(self.surfaces[img_name])
        self.drawer.ctx.paint()

    def setup_images(self):
        names = (
            "display-brightness-high",
            "display-brightness-medium",
            "display-brightness-low",
            "display-brightness-off",
        )
        d_images = images.Loader(self.theme_path)(*names)
        for name, img in d_images.items():
            new_height = self.bar.height - 20
            img.resize(height=new_height)
            # if img.width > self.length:
                # self.length = img.width + self.actual_padding * 2
            self.surfaces[name] = img.pattern

    def get_brightness(self):
        float_brightness = float(subprocess.getoutput(self.get_brightness_command))
        # str_brightness = "{:.0f}%".format(float_brightness)
        # return str_brightness
        return float_brightness

    def draw(self):
        self.drawer.draw(offsetx=self.offset, offsety=self.offsety, width=self.length)

    @expose_command()
    def force_update(self):
        self.update()


class BriText(base._TextBox):
    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        # ("padding", 3, "Padding left and right. Calculated if None."),
        (
            "get_brightness_command",
            "brillo",
        ),
    ]

    def __init__(self, **config):
        base._TextBox.__init__(self, "BACKLIGHT?", **config)
        self.add_defaults(BriText.defaults)
        self.length_type = bar.STATIC
        self.length = 44

    def _configure(self, qtile, bar):
        base._TextBox._configure(self, qtile, bar)
        self.update()

    def update(self):
        self.brightness = self.get_brightness()
        self._update_drawer()
        self.bar.draw()

    def _update_drawer(self):
        self.text = self.brightness
    
    def get_brightness(self):
        float_brightness = float(subprocess.getoutput(self.get_brightness_command))
        str_brightness = "{:.0f}%".format(float_brightness)
        return str_brightness

    @expose_command()
    def force_update(self):
        self.update()
