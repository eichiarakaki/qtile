from libqtile import widget, bar
from settings.theme import colors


def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator(padding=5):
    return widget.Sep(**base(), linewidth=0, padding=padding)


def icon(fg='text', bg='dark', fontsize=16, text="?", padding=3, fontshadow=None, font='Fira Code'):
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

def workspaces(): 
    return [
        widget.Spacer(**base()),
        widget.GroupBox(
            **base(fg='light'),
            font='Fira Code',
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
            this_current_screen_border=colors['dark'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        widget.Spacer(**base()),
    ]

primary_widgets = [

    separator(padding=20),

    icon(bg='dark', fg='color2', text='墳'),

    widget.Volume(**base(bg='dark', fg='color2'), font='Font Awesome 5 Free Solid'),

    icon(bg='dark', fg='color2', text=' - '), 

    widget.Battery(
        **base(bg='dark', fg='color2'), 
        discharge_char='',
        charge_char=' ',
        format='{char} {percent:2.0%}',
        update_interval=60, 
        font='Font Awesome 5 Free Solid'
        ),
    
    *workspaces(),

    widget.TextBox(
        text="  ",
        font="Font Awesome 5 Free Solid",
        foreground=colors['color1'],
        background=colors['dark'],
        ),

    widget.Clock(
        format="%a, %b %d",
        foreground=colors['color1'],
        background=colors['dark'],
        ),

    icon(bg='dark', fg='color1', text=' - '), 

    widget.Clock(
        format="%I:%M %p",
        foreground=colors['color1'],
        background=colors['dark'],
        ),

    separator(padding=20),

]


secondary_widgets = [
    *workspaces(),
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
