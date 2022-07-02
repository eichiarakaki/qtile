from libqtile import bar, hook, pangocffi
from libqtile.widget import base
import getpass

USERNAME = getpass.getuser()

def gen(text: str, sep: str) -> str:
    sep = text.find(sep)
    return text[:sep] if sep != -1 else text

def exclude_titles(title : str) -> bool:
    """Everything with X or the full path"""
    exclude_list = [
        'home',
        USERNAME,
        'fish',
        'zsh',
        'cava',
        '~',
        #'python',
        #'nvim'
    ]

    for i in exclude_list:
        if title.find(i) != -1:
            return True
            
    return False


class WindowName(base._TextBox):
    """Displays the name of the window that currently has focus"""

    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ("show_state", False, "show window status before window name"),
        (
            "for_current_screen",
            False,
            "instead of this bars screen use currently active screen",
        ),
        (
            "empty_group_string",
            " ",
            "string to display when no windows are focused on current group",
        ),
        ("max_chars", 0, "max number of characters to display in the widget"),
    ]

    def __init__(self, width=bar.STRETCH, **config):
        base._TextBox.__init__(self, width=width, **config)
        self.add_defaults(WindowName.defaults)

    def _configure(self, qtile, bar):
        base._TextBox._configure(self, qtile, bar)
        hook.subscribe.startup_once(self.update)
        hook.subscribe.client_name_updated(self.update)
        hook.subscribe.focus_change(self.update)
        hook.subscribe.float_change(self.update)

        @hook.subscribe.current_screen_change
        def on_screen_changed():
            if self.for_current_screen:
                self.update()

    def update(self, *args):
        if self.for_current_screen:
            w = self.qtile.current_screen.group.current_window
        else:
            w = self.bar.screen.group.current_window
        state = ""
        if self.show_state and w is not None:
            if w.maximized:
                state = ""# "[] "
            elif w.minimized:
                state = ""# "_ "
            elif w.floating:
                state = ""# "V "
        unescaped = "%s%s" % (
            state,
            w.name if w and w.name else self.empty_group_string,
        )
        full_string = pangocffi.markup_escape_text(unescaped)
        just_title = gen(full_string, ' - ')

        if exclude_titles(just_title):
            self.text = self.empty_group_string.center(self.max_chars, ' ')
        elif len(just_title) > self.max_chars > 0:
            trunc_string = just_title[: self.max_chars] + "…"
            self.text = trunc_string
        else:
            self.text = just_title.center(self.max_chars, ' ')
        
        self.bar.draw()
