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

# "壹", "貳", "參", "肆", "伍", "陸", "柒", "捌", "玖"


# "壹", 
# "貳", 
# "參", 
# "肆", 
# "伍", 
# "陸", 
# "柒", 
# "捌", 
# "玖"

all_groups = [
                ('壹', {'layout': 'monadtall'})
              , ('貳', {'layout': 'monadtall'})
              , ('參', {'layout': 'monadtall'})
              , ('肆', {'layout': 'monadtall'})
              , ('伍', {'layout': 'bsp'      })
              , ('陸', {'layout': 'bsp'      })
              , ('柒', {'layout': 'bsp'      })
              , ('捌', {'layout': 'bsp'      })
              , ('玖', {'layout': 'monadtall'})
            ]

groups = [Group(name, **kwargs) for name, kwargs in all_groups]

for i, (name, kwargs) in enumerate(all_groups, 1):
    actual_key = str(i)
    keys.extend([
        Key([modkey], actual_key, lazy.group[name].toscreen()),        # Switch to workspace X
        Key([modkey, "shift"], actual_key, lazy.window.togroup(name)) # Send window to workspace X
    ])
