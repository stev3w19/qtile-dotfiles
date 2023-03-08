##### libqtile
from libqtile import bar
from libqtile.lazy import lazy
from libqtile.config import Screen

##### qtile_extras
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget import modify

##### My custom widgets
from custom_widgets import Brillo 
from custom_widgets import VolumeIcon

##### My modules
from theme_prefs import *

##### Widget defaults
widget_defaults = dict(
    font            = font_text,
    fontsize        = 18,
    padding         = 0,
    foreground      = colors[25],
    background      = colors[0],
)
extension_defaults = widget_defaults.copy()

### extras decorations definition
for i in range(len(colors)):
    locals()["ul_%i" % i] = BorderDecoration(colour=colors[i], border_width = [0, 0, 4, 0], padding_x = 0)
    
##### Bar
screens = [
    Screen(
        top=bar.Bar(
            [   ##### list of widgets
                ### layoutbox
                widget.Spacer(
                    length = 20,
                ),
                widget.CurrentLayoutIcon(
                    scale = 0.6,
                    padding = 0,
                ),

                ### groupbox
                widget.Spacer(
                    length = 20,
                ),
                widget.GroupBox(
                    fontsize = 50,

                    disable_drag = True,

                    padding = 0,
                    borderwidth = 6,
                    inactive = colors[7],
                    highlight_method = "line",
                    highlight_color = [colors[4], colors[4]],
                    this_current_screen_border = colors[23],
                    this_screen_border = colors[23],
                ),
            ### centre space
                widget.Spacer(
                ),
                ### mpd
                widget.Mpd2(
                    # foreground = colors[14],
                    play_states = {'pause': '▶', 'play': '⏸', 'stop': '■'},
                    status_format = '{play_status} {artist} - {title}',
                    decorations = [
                        ul_25,
                    ],
                ),

            ### right space
                widget.Spacer(
                ),
                ### systray
                widget.StatusNotifier(
                    icon_size = 25,
                    decorations = [
                        ul_17,
                    ],
                ),

            ### status icons
                ### wlan
                widget.Spacer(
                    length = 12,
                ),
                widget.WiFiIcon(
                    padding_y = 14,
                    padding_x = 4,
                    interface = "wlp2s0",
                    update_interval = 10,

                    active_colour = colors[18],
                    inactive_colour = colors[6],
                    decorations = [
                        ul_18,
                    ]
                ),
                widget.Wlan(
                    foreground = colors[18],
                    interface = "wlp2s0",
                    format='{essid}',
                    update_interval = 10,
                    decorations = [
                        ul_18,
                    ]
                ),
                widget.Spacer(
                    length = 12,
                ),

                ### brightness
                modify(
                    Brillo.BriIcon,
                    theme_path = assets_path + "/display-brightness",
                    decorations = [
                        ul_20,
                    ]
                ),
                modify(
                    Brillo.BriText,
                    foreground = colors[20],
                    decorations = [
                        ul_20,
                    ]
                ),

                ## volume
                widget.Spacer(
                    length = 12,
                ),
                # modify(
                #     VolumeIcon.VolIcon,
                #         theme_path = assets_path + "/audio-volume",
                #         decorations = [
                #             ul_22,
                #         ]
                #     ),

                # modify(
                #     VolumeIcon.VolText,
                #         foreground = colors[22],
                #         decorations = [
                #             ul_22,
                #         ]
                # ),
                widget.ALSAWidget(
                    font = "Arial",
                    background = colors[0],
                ),

                ### battery
                widget.Spacer(
                    length = 12,
                ),
                widget.BatteryIcon(
                    theme_path = assets_path + "/battery",
                    update_interval = 120,
                    decorations = [
                        ul_23,
                    ],
                ),       
                widget.Battery(
                    foreground = colors[23],
                    format = "{percent:2.0%}",
                    decorations = [
                        ul_23,
                    ],
                ),

                ### clock
                widget.Spacer(
                    length = 12,
                ),
                widget.Image(
                    filename = assets_path + "/clock/clock.svg",
                    margin_y = 10,
                    margin_x = 4,
                    decorations = [
                        ul_25,
                    ],
                ),
                widget.Clock(
                    foreground = colors[25],
                    decorations = [
                        ul_25,
                    ],
                ),
                widget.Spacer(
                    length = 20,
                ),
            ],
            # 46, # bar height
            48,
            margin      = [0, 0, 10, 0],
            # border_color = colors[0],
            # border_width = [2, 0, 0, 0],
            background  = colors[0],
            opacity     = 0.90,
        ),
    ),
]