from libqtile.command import lazy
from libqtile.widget import (
      Sep
    , GroupBox
    , CurrentLayoutIcon
    , TextBox
    , Spacer
    , Clock
    , TextBox
    , Battery
    , CurrentLayout
)
from custom.windowname import WindowName as CustomWindowName
# from custom.battery import Battery as CustomBattery

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


def base(fg=FG, bg=BG, font='Iosevka'): 
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
      "padding":                     17
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
    , "fontsize":                    16

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
            visible_groups=["壹"],
            block_highlight_text_color=GREEN,
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["貳"],
            block_highlight_text_color=BLUE,
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["參"],
            block_highlight_text_color=GREEN,
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["肆"],
            block_highlight_text_color=BLUE,
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["伍"],
            block_highlight_text_color=GREEN,
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["陸"],
            block_highlight_text_color=BLUE,
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["柒"],
            block_highlight_text_color=GREEN,
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["捌"],
            block_highlight_text_color=BLUE,
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["玖"],
            block_highlight_text_color=GREEN,
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
    CurrentLayout(
        **base(),
        fontize=13,
        fmt='{}'
    ),

    # CustomWindowName(
    #     **base(),
    #     max_chars=25,
    #     fontsize=13,
    #     empty_group_string='Desktop',
    # ),

    Spacer(**base()),
    *workspaces(),
    
    Spacer(**base()),

    # Boxes
    *apps(padding=13),


    txt(text='|', fontsize=15, fg=BORDERS, padding=8),
    # Time
    #txt(text=' ', fontsize=14, fg=CYAN),
    Clock(
          **base(fg=CYAN)
        , fontsize=13
        #, format='%B %-d, %I:%M'
        , format='%I:%M'
    ),

    
    txt(text='|', fontsize=15, fg=BORDERS, padding=8),
    # Battery
    #txt(text='', padding=5, fontsize=13, fg=GREEN),
    Battery(
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
