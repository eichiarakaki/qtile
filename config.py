from libqtile.hook import subscribe
from os.path import join
from re import search
from settings.path import qtile_path
from settings.screens import screens
from settings.mouse import mouse
from settings.groups import groups
from settings.keys import (
    modkey, 
    keys,
)
from settings.layouts import (
    layouts, 
    floating_layout,
)
from settings.widgets import (
    widget_defaults, 
    extension_defaults,
)
from subprocess import (
    call,
    PIPE,
    Popen,
)


def is_running(process):
    s = Popen(["ps", "axuw"], stdout=PIPE)
    for x in s.stdout:
        if search(process, x):
            return True
    return False

def execute_once(process):
    if not is_running(process):
        return Popen(process.split())



@subscribe.startup_once
def autostart():
    call([join(qtile_path, 'startup.sh')])
    # execute_once('echo something.')


main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = 'smart'
# java app don't work correctly if the wmname isn't set to a name that happens to
# be on java's whitelist (LG3D is a 3D non-reparenting WM written in java).
wmname = 'LG3D'
