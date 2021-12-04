from libqtile.widget import (
    Sep, 
    # GroupBox, 
    CurrentLayoutIcon,
    # TextBox, 
    # Spacer, 
    # GenPollText,
)
from custom.windowname import WindowName as CustomWindowName
from settings.path import qtile_path
from os import path
from settings.theme import colors

BGMGR = 'color0'
FGMGR = 'color1'

""" Useless Code, take this code as an example
import datetime




def texts(fg=FGMGR, bg=BGMGR, fontsize=16, text="?", padding=3, font='Fira Code'):
    return TextBox(
        **base(fg=fg, bg=bg, font=font),
        fontsize=fontsize,
        text=text,
        padding=padding
    )


group_box_settings = {
    "padding": 15,
    "borderwidth": 0,
    "disable_drag": True,
    "font": 'Fira Code',
    "rounded": True,
    "highlight_color": colors[FGMGR],
    "this_screen_border": colors['color4'],
    "other_current_screen_border": colors[BGMGR],
    "other_screen_border": colors[BGMGR],
    "foreground": colors[FGMGR],
    "background": colors[BGMGR],
    "urgent_border": colors[BGMGR],
    "fontsize": 15,


    "margin_x": 0,
    "margin_y": 1,
    "this_current_screen_border": colors[BGMGR],
    "urgent_text": colors[FGMGR],
    "inactive": colors['color3'],
    "active": colors['color1']
}

def workspaces():
    return [
        GroupBox(
            **group_box_settings,
            visible_groups=["一"],
            block_highlight_text_color=colors['color2'],
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["二"],
            block_highlight_text_color=colors['color4'],
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["三"],
            block_highlight_text_color=colors['color5'],
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["四"],
            block_highlight_text_color=colors['color6'],
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["五"],
            block_highlight_text_color=colors['color7'],
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["六"],
            block_highlight_text_color=colors['color4'],
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["七"],
            block_highlight_text_color=colors['color9'],
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["八"],
            block_highlight_text_color=colors['color5'],
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["九"],
            block_highlight_text_color=colors['color7'],
        )
        
    ]
    
# def widgets():
#     return [
#         text(fg='color2', bg=BGMGR, fontsize=15, text='東', padding=3),
#         separator(padding=12, bg=BGMGR),
#         text(fg='color5', bg=BGMGR, fontsize=15, text='西', padding=3),
#         separator(padding=12, bg=BGMGR),
#         text(fg='color4', bg=BGMGR, fontsize=16, text='南', padding=3),
#         separator(padding=12, bg=BGMGR),
#         text(fg='color6', bg=BGMGR, fontsize=16, text='北', padding=3),
#     ]
"""

def base(fg=FGMGR, bg=BGMGR, font='Fira Code'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg],
        'font': font
    }

def separator(padding=5, bg=BGMGR):
    return Sep(**base(bg=bg), linewidth=0, padding=padding)

bar_widgets = [
    separator(padding=15, bg=BGMGR),

    CurrentLayoutIcon(
        custom_icon_paths=[path.join(qtile_path, "icons", "Layouts-cyan")],
        **base(bg=BGMGR, fg=FGMGR),
        padding=0,
        scale=0.37,
        fontsize=0.5
    ),
    #----

    # *workspaces(),
    separator(padding=110, bg=BGMGR),
    
    CustomWindowName(
        **base(),
        max_chars=25,
        fontsize=13,
        empty_group_string='Desktop',
    ),
]

widget_defaults = {
    'font': 'Fira Code',
    'fontsize': 14,
    'padding': 1,
}

extension_defaults = widget_defaults.copy()
