from path import qtile_path
from json import load
from os.path import (
    join, 
    isfile,
)


def load_theme():
    file_name = 'mirai'
    dir_name = 'themes'
    theme_path = join(
        qtile_path, 
        dir_name, 
        '%s.json' % file_name
    )

    if not isfile(theme_path):
        raise Exception('"%s" does not exist.' % theme_path)

    with open(join(theme_path)) as f:
        return load(f)


if __name__ == 'settings.theme':
    colors = load_theme()

    FG      = colors['foreground'][0]
    BG      = colors['background'][0]
    BLACK   = colors['black'][0]
    RED     = colors['red'][0]
    GREEN   = colors['green'][0]
    YELLOW  = colors['yellow'][0]
    BLUE    = colors['blue'][0]
    MAGENTA = colors['magenta'][0]
    ORANGE  = colors['orange'][0]
    CYAN    = colors['cyan'][0]
    GREY    = colors['grey'][0]
    WHITE   = colors['white'][0]
    BORDERS = colors['borders'][0]

    SOFT_RED     = colors['red'][1]
    SOFT_GREEN   = colors['green'][1]
    SOFT_YELLOW  = colors['yellow'][1]
    SOFT_BLUE    = colors['blue'][1]
    SOFT_MAGENTA = colors['magenta'][1]
    ORANGE       = colors['orange'][1]
    SOFT_CYAN    = colors['cyan'][1]
    SOFT_WHITE   = colors['white'][1]
    SOFT_BORDERS = colors['borders'][1]