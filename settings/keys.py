from libqtile.config import Key
from libqtile.command import lazy
from settings.keyboard import next_layout
from settings.path import qtile_path
modkey = 'mod4'
altkey = 'mod1'


keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch focus between windows in current stack pane
    ([modkey], 'j', lazy.layout.left()),
    ([modkey], 'k', lazy.layout.right()),
    ([modkey], 'h', lazy.layout.down()),
    ([modkey], 'l', lazy.layout.up()),

    # Change window sizes
    ([altkey, modkey], 'j', lazy.layout.grow()),
    ([altkey, modkey], 'k', lazy.layout.shrink()),
    #(['control'], 'n', lazy.layout.normalize()),
    #(['control'], 'm', lazy.layout.maximize()),

    # Move windows in current stack
    ([altkey], 'j', lazy.layout.shuffle_left()),
    ([altkey], 'k', lazy.layout.shuffle_right()),
    ([altkey], 'h', lazy.layout.shuffle_down()),
    ([altkey], 'l', lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([modkey], 'Tab', lazy.next_layout()),

    # Toggle a window to floating & tiling
    ([modkey], 'f', lazy.window.toggle_floating()),

    # Kill window
    ([modkey], 'w', lazy.window.kill()),

    # Restart Qtile
    ([modkey], 'F1', lazy.restart()),
    

    # ------------ App Configs ------------

    # Launcher
    ([modkey], "m", lazy.spawn("rofi -show drun")),

    # Browser
    ([modkey], 'b', lazy.spawn('google-chrome-stable')),

    # Terminal
    ([modkey], 'Return', lazy.spawn('kitty')),

    # Redshift
    ([modkey], 'r', lazy.spawn('redshift -O 4000')),
    ([modkey, 'shift'], 'r', lazy.spawn('redshift -x')),

    # Screenshot
    ([modkey], 's', lazy.spawn('flameshot gui')),
    
    ([modkey], 't', lazy.spawn(f'{qtile_path}/scripts/timenotify')),

    # keyboard layouts
    ([modkey], 'space', lazy.function(next_layout, ['es', 'us'])),


    # ------------ Hardware Configs ------------

    # Volume
    ([], 'XF86AudioLowerVolume', lazy.spawn(
        'pactl set-sink-volume @DEFAULT_SINK@ -5%'
    )),
    ([], 'XF86AudioRaiseVolume', lazy.spawn(
        'pactl set-sink-volume @DEFAULT_SINK@ +5%'
    )),
    ([], 'XF86AudioMute', lazy.spawn(
        'pactl set-sink-mute @DEFAULT_SINK@ toggle'
    )),

    # Brightness
    ([], 'F8', lazy.spawn('brightnessctl set 5%-')),
    ([], 'F9', lazy.spawn('brightnessctl set +5%')),
]]
