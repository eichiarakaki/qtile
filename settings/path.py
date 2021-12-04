from os.path import join, expanduser


CONFIG = join(expanduser('~'), '.config')

qtile_path = join(CONFIG, 'qtile')
picom_path = join(CONFIG, 'picom')
dunst_path = join(CONFIG, 'dunst')