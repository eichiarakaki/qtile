from libqtile.layout import (
    Max, 
    MonadTall, 
    MonadWide, 
    Bsp, 
    Floating,
)
from libqtile.config import Match
from settings.theme import colors

layout_cfg = {
    'border_focus': colors['borders'][0],
    'border_normal': colors['borders'][1],
    'border_width': 0, # Border width null
    'margin': 10,
}

layouts = [
    Max(**layout_cfg),
    MonadTall(**layout_cfg),
    MonadWide(**layout_cfg),
    Bsp(**layout_cfg),
]

floating_layout = Floating(
    float_rules = [
        *Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
    **layout_cfg,
)
