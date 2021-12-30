from path import qtile_path
from json import load
from os.path import (
    join, 
    isfile,
)


def load_theme():
    file_name = 'default'
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
elif __name__ == '__main__':
    colors = load_theme()