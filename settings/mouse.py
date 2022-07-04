from libqtile.config import (
    Drag, 
    Click,
)
from libqtile.command import lazy
from settings.keys import modkey


mouse = [
    Drag(
        [modkey],
        "Button1",
        lazy.window.set_position(),
        start=lazy.window.get_position()
    ),
    Drag(
        [modkey],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),
    Click([modkey], 
         "Button2", 
         lazy.window.toggle_focus_floating()
    )
]
