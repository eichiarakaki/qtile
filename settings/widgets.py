from libqtile import widget, bar
from settings.theme import colors
#from custom.windowname import WindowName as CustomWindowName


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


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-2
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
        #icon(fg="symbol", text=' arcн lιnυх', fontsize=17.3, padding=5),

        widget.GroupBox(
            #center_aligned=True,
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

        widget.WindowName(
            **base(fg='ws_focus'), 
            fontsize=14, 
            font='Fira Code',
            format='{state}',
            width=bar.CALCULATED,
            max_chars=60,
            empty_group_string='Desktop',
            fmt='{}'
            ),
        widget.Spacer(**base()),

    ]

""" Check Updates"""
    #powerline('color4', 'dark'),

    #icon(bg="color4", text=' '), # Icon: nf-fa-download
    
    #widget.CheckUpdates(
    #    background=colors['color4'],
    #    colour_have_updates=colors['text'],
    #    colour_no_updates=colors['text'],
    #    no_update_string='0',
    #    display_format='{updates}',
    #    update_interval=900,
    #    custom_command='checkupdates',
    #),

    #powerline('dark', 'color4'),
""""""

"""Layout mode"""
    #widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

    #widget.CurrentLayout(**base(bg='color2'), padding=5),

    #powerline('dark', 'color2'),
    #powerline('color2', 'dark'),
""""""

""" Net """
# icon(bg="color3", text=' '),  # Icon: nf-fa-feed
    
# widget.Net(**base(bg='color3'), interface='enp13s0f1'),
""""""

primary_widgets = [
    *workspaces(),

    widget.CPU(**base(bg='dark', fg='color3')),

    icon(bg='dark', fg='color3', text=' - '), 

    icon(bg='dark', fg='color3', text='Mem'), 

    widget.Memory(**base(bg='dark', fg='color3'), font='Fira Code'),

    separator(padding=20),

    icon(bg='dark', fg='color2', text='墳 '),

    widget.Volume(**base(bg='dark', fg='color2'), font='Fira Code'),

    icon(bg='dark', fg='color2', text=' - '), 

    widget.Battery(
        **base(bg='dark', fg='color2'), 
        discharge_char='',
        charge_char=' ',
        format='{char} {percent:2.0%}',
        update_interval=60, 
        font='Fira Code'
        ),

    separator(padding=20),

    #icon(bg="dark", fg="color1", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(
        **base(bg='dark', fg='color1'), 
        format=' %A %B %d - %H:%M ', 
        font='Fira Code'
        ),

    separator(padding=20),

    #widget.Systray(background=colors['dark'], padding=5),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='dark', fg='color1'), format=' %A %B %d - %H:%M '),

    #powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
