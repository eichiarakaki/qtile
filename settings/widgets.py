from libqtile import widget, bar
from settings.theme import colors

GBMGR = 'bg'
FGMGR = 'fg'

def base(fg=FGMGR, bg=GBMGR): 
    return {
        'foreground': colors[fg],
        'background': colors[bg],
        'font': 'Font Awesome 5 Free Solid'
    }


def separator(padding=5, bg=GBMGR):
    return widget.Sep(**base(bg=bg), linewidth=0, padding=padding)


def icon(fg=FGMGR, bg=GBMGR, fontsize=16, text="?", padding=3, fontshadow=None):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=padding,
        fontshadow=fontshadow
    )

"""
my_colors = [
    ["#2e3440", "#2e3440"],  # background
    ["#d8dee9", "#d8dee9"],  # foreground
    ["#3b4252", "#3b4252"],  # background lighter
    ["#bf616a", "#bf616a"],  # red
    ["#a3be8c", "#a3be8c"],  # green
    ["#ebcb8b", "#ebcb8b"],  # yellow
    ["#81a1c1", "#81a1c1"],  # blue
    ["#b48ead", "#b48ead"],  # magenta
    ["#88c0d0", "#88c0d0"],  # cyan
    ["#e5e9f0", "#e5e9f0"],  # white
    ["#4c566a", "#4c566a"],  # grey
    ["#d08770", "#d08770"],  # orange
    ["#8fbcbb", "#8fbcbb"],  # super cyan
    ["#5e81ac", "#5e81ac"],  # super blue
    ["#242831", "#242831"],  # super dark background
]
"""

def barA():
    return [
        separator(padding=8, bg=GBMGR),
        widget.GroupBox(
            **base(fg=FGMGR, bg=GBMGR),
            fontsize=19,
            margin_y=3,
            margin=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['fg'],
            inactive=colors['fg'],
            rounded=True,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            block_highlight_text_color=colors['urgent'],
            this_current_screen_border=colors[GBMGR],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors[GBMGR],
            other_screen_border=colors[GBMGR],
            disable_drag=True
        ),
        widget.Spacer(**base(bg=GBMGR)),
    ]


def barB():
    return [
        separator(padding=25, bg=GBMGR),

        widget.CPU(**base(bg=GBMGR, fg=FGMGR), 
                   fontsize=12,
                   format='💻 {freq_current}GHz',
                   update_interval=1
                   ),

        separator(padding=20, bg=GBMGR),

        icon(bg=GBMGR, fg='color6', text=' ', fontsize=19), 

        widget.Memory(**base(bg=GBMGR, fg=FGMGR),
                     fontsize=12,
        ),

        widget.Spacer(**base(bg=GBMGR)),

        widget.TextBox(
            text="  ",
            foreground=colors['color1'],
            background=colors[GBMGR],
            ),

        widget.Clock(
            format="%A, %B %d",
            foreground=colors[FGMGR],
            background=colors[GBMGR],
            ),

        icon(bg=GBMGR, fg=FGMGR, text=' - '), 

        widget.Clock(
            format="%I:%M %p",
            foreground=colors[FGMGR],
            background=colors[GBMGR],
            ),
            
        widget.Spacer(**base(bg=GBMGR)),

        icon(bg=GBMGR, fg='color2', text='墳  ', fontsize=19),

        widget.Volume(**base(bg=GBMGR, fg=FGMGR)),

        separator(padding=20, bg=GBMGR),

        icon(bg=GBMGR, fg='color5', text=' ', fontsize=13), 

        widget.Battery(
            **base(bg=GBMGR, fg=FGMGR), 
            discharge_char='',
            charge_char='',
            format='{char} {percent:2.0%}',
            update_interval=60, 
            ),

        separator(padding=20, bg=GBMGR),
    ]


primary_widgets_barA = [
    *barA()
]
primary_widgets_barB = [
    *barB()
]

secondary_widgets = [
    *barA(),
"""
    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='dark', fg='color1'), format=' %A %B %d - %H:%M '),

    #powerline('dark', 'color2'),
"""
]

widget_defaults = {
    'font': 'Font Awesome 5 Free Solid',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
