from libqtile.layout import (
    Max, 
    MonadTall, 
    MonadWide, 
    Bsp, 
    Floating,
)
from libqtile.config import Match
from settings.theme import BORDERS, SOFT_BORDERS


layout_cfg = {
    'border_focus': BORDERS,
    'border_normal': SOFT_BORDERS,
    'border_width': 0, # Border width 0 = null
    'margin': 5,
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
