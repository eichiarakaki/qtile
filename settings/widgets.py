from libqtile import widget, bar
from settings.theme import colors


def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator(padding=5, bg='dark'):
    return widget.Sep(**base(bg=bg), linewidth=0, padding=padding)


def icon(fg='text', bg='dark', fontsize=16, text="?", padding=3, fontshadow=None, font='Font Awesome 5 Free Solid'):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=padding,
        fontshadow=fontshadow,
        font=font
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
    bgmgr = 'bg'
    return [
    
        widget.GroupBox(
            **base(fg='light', bg=bgmgr),
            font='Font Awesome 5 Free Solid',
            fontsize=19,
            margin_y=3,
            margin=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=True,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            block_highlight_text_color=colors['ws_focus'],
            this_current_screen_border=colors[bgmgr],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors[bgmgr],
            other_screen_border=colors[bgmgr],
            disable_drag=True
        ),
        widget.Spacer(**base(bg=bgmgr)),
    ]


def barB():
    bgmgr = 'bg'
    return [
        widget.Spacer(**base(bg=bgmgr)),

        icon(bg=bgmgr, fg='color2', text='墳'),

        widget.Volume(**base(bg=bgmgr, fg='color2'), font='Font Awesome 5 Free Solid'),

        icon(bg=bgmgr, fg='color2', text=' - '), 

        widget.Battery(
            **base(bg=bgmgr, fg='color2'), 
            discharge_char='',
            charge_char=' ',
            format='{char} {percent:2.0%}',
            update_interval=60, 
            font='Font Awesome 5 Free Solid'
            ),
        
        separator(padding=25, bg=bgmgr),

        widget.TextBox(
            text="  ",
            font="Font Awesome 5 Free Solid",
            foreground=colors['color1'],
            background=colors[bgmgr],
            ),

        widget.Clock(
            format="%a, %b %d",
            foreground=colors['color1'],
            background=colors[bgmgr],
            ),

        icon(bg=bgmgr, fg='color1', text=' - '), 

        widget.Clock(
            format="%I:%M %p",
            foreground=colors['color1'],
            background=colors[bgmgr],
            ),

        separator(padding=20, bg=bgmgr),
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
