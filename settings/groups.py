from libqtile.command import lazy
from libqtile.config import (
    Key, 
    Group,
)
from settings.keys import (
    modkey, 
    keys,
)


# "Ⅰ", "Ⅱ", "Ⅲ", "Ⅳ", "Ⅴ", "Ⅵ", "Ⅶ", "Ⅷ", "Ⅸ"

# "Ⅰ"
# "Ⅱ"
# "Ⅲ"
#  Ⅳ"
# "Ⅴ"
# "Ⅵ"
# "Ⅶ"
# "Ⅷ"
# "Ⅸ"


# "一", "二", "三", "四", "五", "六", "七", "八", "九"

# "一"
# "二"
# "三"
# "四"
# "五"
# "六"
# "七"
# "八"
# "九"


all_groups = [
                ('Ⅰ', {'layout': 'monadtall'})
              , ('Ⅱ', {'layout': 'monadtall'})
              , ('Ⅲ', {'layout': 'monadtall'})
              , ('Ⅳ', {'layout': 'monadtall'})
              , ('Ⅴ', {'layout': 'bsp'      })
              , ('Ⅵ', {'layout': 'bsp'      })
              , ('Ⅶ', {'layout': 'bsp'      })
              , ('Ⅷ', {'layout': 'bsp'      })
              , ('Ⅸ', {'layout': 'monadtall'})
            ]

groups = [Group(name, **kwargs) for name, kwargs in all_groups]

for i, (name, kwargs) in enumerate(all_groups, 1):
    actual_key = str(i)
    keys.extend([
        Key([modkey], actual_key, lazy.group[name].toscreen()),        # Switch to workspace X
        Key([modkey, "shift"], actual_key, lazy.window.togroup(name)) # Send window to workspace X
    ])
