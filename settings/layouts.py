from libqtile import layout
from libqtile.config import Match
from settings.theme import colors

layout_conf = {
    'border_focus': colors['dark'][0],
    'border_width': 1,
    'margin': 15
}

layouts = [
    layout.Max(),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    #CustomBsp(**layout_conf, fair=False),
    # layout.Bsp(**layout_conf),
    # layout.Matrix(columns=2, **layout_conf),
    # layout.RatioTile(**layout_conf),
    # layout.Columns(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
    border_focus=colors["dark"][0]
)
