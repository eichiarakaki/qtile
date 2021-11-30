from libqtile.layout import (
    Max, 
    MonadTall, 
    MonadWide, 
    Bsp, 
    Floating,
)
from libqtile.config import Match
from settings.theme import colors

layout_conf = {
    'border_focus': colors['color10'][0],
    'border_normal': colors['color3'][0],
    'border_width': 0,
    'margin': 10,
}

layouts = [
    Max(),
    MonadTall(**layout_conf),
    MonadWide(**layout_conf),
    Bsp(**layout_conf),
]

floating_layout = Floating(
    float_rules=[
        *Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
    **layout_conf,
)
