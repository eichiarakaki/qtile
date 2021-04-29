from libqtile import widget
from settings.theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?", padding=3):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=padding
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-2
    )


def workspaces(): 
    return [
        icon(fg="color3", text=' arcн lιnυх', fontsize=17.3, padding=-2),
        separator(),

        widget.GroupBox(
            #center_aligned=True,
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.Spacer(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
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

    separator(),

    powerline('color3', 'dark'),

    widget.CPU(**base(bg='color3')),

    icon(bg="color3", text=' - '), 

    icon(bg="color3", text='Mem'), 

    widget.Memory(**base(bg='color3')),

    powerline('dark', 'color3'),
    powerline('color2', 'dark'),

    icon(bg="color2", text='墳 '),

    widget.Volume(**base(bg='color2')),

    icon(bg="color2", text=' - '), 

    icon(bg="color2", text=' '),

    widget.Battery(**base(bg='color2')),

    powerline('dark', 'color2'),
    powerline('color1', 'dark'),

    icon(bg="color1", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color1'), format=' %A %B %d - %H:%M '),

    powerline('dark', 'color1'),

    #widget.Systray(background=colors['dark'], padding=5),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
