from libqtile.command import lazy
from libqtile.widget import (
      Sep
    , GroupBox
    , CurrentLayoutIcon
    , TextBox
    , Spacer
    , Clock
    , TextBox
)
from custom.windowname import WindowName as CustomWindowName
from custom.battery import Battery as CustomBattery

from settings.path import qtile_path
from os import path
from settings.theme import (
      FG
    , BG
    , BLACK
    , RED
    , GREEN
    , YELLOW
    , BLUE
    , MAGENTA
    , CYAN
    , ORANGE
    , GREY
    , WHITE
    , BORDERS
)


def base(fg=FG, bg=BG, font='Cascadia Mono PL'): 
    return {
        'foreground': fg,
        'background': bg,
        'font': font
    }


def txt(fg=FG, bg=BG, fontsize=16, text="?", padding=3, font='Cascadia Mono PL'):
    return TextBox(
        **base(fg=fg, bg=bg, font=font),
        fontsize=fontsize,
        text=text,
        padding=padding
    )


group_box_settings = {
      "padding":                     10
    , "borderwidth":                 0
    , "disable_drag":                True
    , "font":                        'Cascadia Mono PL'
    , "rounded":                     True
    , "highlight_color":             FG

    , "this_screen_border":          MAGENTA
    
    , "other_current_screen_border": BG
    , "other_screen_border":         BG
    , "foreground":                  FG
    , "background":                  BG
    , "urgent_border":               BG
    , "fontsize":                    15

    , "margin_x":                    0
    , "margin_y":                    1
    , "this_current_screen_border":  BG
    , "urgent_text":                 FG
    , "inactive":                    BORDERS
    , "active":                      GREY
}


def workspaces():
    return [
        GroupBox(
            **group_box_settings,
            visible_groups=["一"],
            block_highlight_text_color=YELLOW,
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["二"],
            block_highlight_text_color=YELLOW,
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["三"],
            block_highlight_text_color=YELLOW,
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["四"],
            block_highlight_text_color=YELLOW,
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["五"],
            block_highlight_text_color=YELLOW,
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["六"],
            block_highlight_text_color=YELLOW,
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["七"],
            block_highlight_text_color=YELLOW,
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["八"],
            block_highlight_text_color=YELLOW,
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["九"],
            block_highlight_text_color=YELLOW,
        )
        
    ]


def apps(padding: int) -> list:
    return [
        TextBox(
          **base(fg=BLUE)
        , fontsize=17
        , text=''
        , padding=padding
        , mouse_callbacks={'Button1': lazy.spawn('code')},
    ),
    TextBox(
          **base(fg=ORANGE)
        , fontsize=15
        , text=''
        , padding=padding
        , mouse_callbacks={'Button1': lazy.spawn('open https://www.reddit.com/')},
    ),
    TextBox(
          **base(fg=GREEN)
        , fontsize=17
        , text=''
        , padding=padding
        , mouse_callbacks={'Button1': lazy.spawn('spotify')},
    ),
    TextBox(
          **base(fg=WHITE)
        , fontsize=17
        , text=''
        , padding=padding
        , mouse_callbacks={'Button1': lazy.spawn('open https://github.com/')},
    ),
    TextBox(
          **base(fg=RED)
        , fontsize=16
        , text=''
        , padding=padding
        , mouse_callbacks={'Button1': lazy.spawn('open https://www.youtube.com/')},
    ),
    
    ]


def separator(padding=5, bg=BG):
    return Sep(**base(bg=bg), linewidth=0, padding=padding)


bar_widgets = [
    separator(padding=7),

    CurrentLayoutIcon(
        custom_icon_paths=[path.join(qtile_path, "icons", "Layouts-mirai-colorscheme")],
        **base(),
        padding=0,
        scale=0.42,
        fontsize=0.4
    ),

    *workspaces(),
    separator(padding=480),
    
    CustomWindowName(
        **base(),
        max_chars=25,
        fontsize=13,
        empty_group_string='Desktop',
    ),
    Spacer(**base()),

    # Boxes
    *apps(padding=13),


    txt(text='|', fontsize=15, fg=BORDERS, padding=8),
    # Time
    txt(text=' ', fontsize=14, fg=CYAN),
    Clock(
          **base(fg=CYAN)
        , fontsize=13
        , format='%B %-d, %I:%M'
    ),

    
    txt(text='|', fontsize=15, fg=BORDERS, padding=8),
    # Battery
    txt(text='', padding=5, fontsize=13, fg=GREEN),
    CustomBattery(
        **base(fg=GREEN), 
        fontsize=13,
        format='{percent:2.0%}', # {char} {percent:2.0%} {hour:d}:{min:02d} {watt:.2f} W
        update_interval=30,
    
    ),

    separator(padding=15),

]


widget_defaults = {
    'font': 'Cascadia Mono PL',
    'fontsize': 14,
    'padding': 1,
}

extension_defaults = widget_defaults.copy()
