from __future__ import annotations

import contextlib
import os.path
import sys
from typing import TYPE_CHECKING, Callable, List, Optional, Union

from libqtile import hook, utils
from libqtile.backend import base
from libqtile.bar import Bar, BarType
from libqtile.command.base import CommandObject, ItemT


if TYPE_CHECKING:
    from libqtile.group import _Group



class Key:
    """Defines a keybinding.

    Parameters
    ==========
    modifiers:
        A list of modifier specifications. Modifier specifications are one of:
        "shift", "lock", "control", "mod1", "mod2", "mod3", "mod4", "mod5".
    key:
        A key specification, e.g. "a", "Tab", "Return", "space".
    commands:
        A list of lazy command objects generated with the lazy.lazy helper.
        If multiple Call objects are specified, they are run in sequence.
    desc:
        description to be added to the key binding
    """
    def __init__(self, modifiers: List[str], key: str, *commands, desc: str = ""):
        self.modifiers = modifiers
        self.key = key
        self.commands = commands
        self.desc = desc

    def __repr__(self):
        return "<Key (%s, %s)>" % (self.modifiers, self.key)


class ScreenRect:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __repr__(self):
        return '<%s %d,%d %d,%d>' % (
            self.__class__.__name__,
            self.x, self.y,
            self.width, self.height
        )

    def hsplit(self, columnwidth):
        assert columnwidth > 0
        assert columnwidth < self.width
        return (
            self.__class__(self.x, self.y, columnwidth, self.height),
            self.__class__(
                self.x + columnwidth, self.y,
                self.width - columnwidth, self.height
            )
        )

    def vsplit(self, rowheight):
        assert rowheight > 0
        assert rowheight < self.height
        return (
            self.__class__(self.x, self.y, self.width, rowheight),
            self.__class__(
                self.x, self.y + rowheight,
                self.width, self.height - rowheight
            )
        )


class Screen(CommandObject):
    """A physical screen, and its associated paraphernalia.

    Define a screen with a given set of Bars of a specific geometry.  Note that
    bar.Bar objects can only be placed at the top or the bottom of the screen
    (bar.Gap objects can be placed anywhere).  Also, ``x``, ``y``, ``width``,
    and ``height`` aren't specified usually unless you are using 'fake
    screens'.

    The ``wallpaper`` parameter, if given, should be a path to an image file. How this
    image is painted to the screen is specified by the ``wallpaper_mode`` parameter. By
    default, the image will be placed at the screens origin and retain its own
    dimensions. If the mode is 'fill', the image will be centred on the screen and
    resized to fill it. If the mode is 'stretch', the image is stretched to fit all of
    it into the screen.
    """
    group: _Group
    previous_group: _Group
    index: int

    def __init__(self, top: Optional[BarType] = None, bottom: Optional[BarType] = None,
                 left: Optional[BarType] = None, right: Optional[BarType] = None,
                 wallpaper: Optional[str] = None, wallpaper_mode: Optional[str] = None,
                 x: Optional[int] = None, y: Optional[int] = None, width: Optional[int] = None,
                 height: Optional[int] = None):

        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.wallpaper = wallpaper
        self.wallpaper_mode = wallpaper_mode
        self.qtile = None
        # x position of upper left corner can be > 0
        # if one screen is "right" of the other
        self.x = x if x is not None else 0
        self.y = y if y is not None else 0
        self.width = width if width is not None else 0
        self.height = height if height is not None else 0

    def _configure(self, qtile, index, x, y, width, height, group):
        self.qtile = qtile
        self.index = index
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.set_group(group)
        for i in self.gaps:
            i._configure(qtile, self)
        if self.wallpaper:
            self.wallpaper = os.path.expanduser(self.wallpaper)
            self.paint(self.wallpaper, self.wallpaper_mode)

    def paint(self, path, mode=None):
        self.qtile.paint_screen(self, path, mode)

    @property
    def gaps(self):
        return (i for i in [self.top, self.bottom, self.left, self.right] if i)

    @property
    def dx(self):
        return self.x + self.left.size if self.left else self.x

    @property
    def dy(self):
        return self.y + self.top.size if self.top else self.y

    @property
    def dwidth(self):
        val = self.width
        if self.left:
            val -= self.left.size
        if self.right:
            val -= self.right.size
        return val

    @property
    def dheight(self):
        val = self.height
        if self.top:
            val -= self.top.size
        if self.bottom:
            val -= self.bottom.size
        return val

    def get_rect(self):
        return ScreenRect(self.dx, self.dy, self.dwidth, self.dheight)

    def set_group(self, new_group, save_prev=True, warp=True):
        """Put group on this screen"""
        if new_group is None:
            return

        if new_group.screen == self:
            return

        if save_prev and hasattr(self, "group"):
            self.previous_group = self.group

        if new_group.screen:
            # g1 <-> s1 (self)
            # g2 (new_group) <-> s2 to
            # g1 <-> s2
            # g2 <-> s1
            g1 = self.group
            s1 = self
            g2 = new_group
            s2 = new_group.screen

            s2.group = g1
            g1.set_screen(s2, warp)
            s1.group = g2
            g2.set_screen(s1, warp)
        else:
            if hasattr(self, "group"):
                old_group = self.group
                ctx = self.qtile.core.masked()
            else:
                old_group = None
                ctx = contextlib.nullcontext()
            self.group = new_group
            with ctx:
                # display clients of the new group and then hide from old group
                # to remove the screen flickering
                new_group.set_screen(self, warp)

                if old_group is not None:
                    old_group.set_screen(None, warp)

        hook.fire("setgroup")
        hook.fire("focus_change")
        hook.fire("layout_change",
                  self.group.layouts[self.group.current_layout],
                  self.group)

    def toggle_group(self, group=None, warp=True):
        """Switch to the selected group or to the previously active one"""
        if group in (self.group, None) and hasattr(self, "previous_group"):
            group = self.previous_group
        self.set_group(group, warp=warp)


    def _items(self, name: str) -> ItemT:
        if name == "layout" and self.group is not None:
            return True, list(range(len(self.group.layouts)))
        elif name == "window" and self.group is not None:
            return True, [i.wid for i in self.group.windows]
        elif name == "bar":
            return False, [x.position for x in self.gaps]
        elif name == "widget":
            return False, [w.name for g in self.gaps for w in g.widgets if isinstance(g, Bar)]
        elif name == "group":
            return True, [self.group.name]
        return None

    def _select(self, name, sel):
        if name == "layout":
            if sel is None:
                return self.group.layout
            else:
                return utils.lget(self.group.layouts, sel)
        elif name == "window":
            if sel is None:
                return self.group.current_window
            else:
                for i in self.group.windows:
                    if i.wid == sel:
                        return i
        elif name == "bar":
            return getattr(self, sel)
        elif name == "widget":
            for gap in self.gaps:
                if not isinstance(gap, Bar):
                    continue
                for widget in gap.widgets:
                    if widget.name == sel:
                        return widget
        elif name == "group":
            if sel is None:
                return self.group
            else:
                return self.group if sel == self.group.name else None

    def resize(self, x=None, y=None, w=None, h=None):
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        if w is None:
            w = self.width
        if h is None:
            h = self.height
        self._configure(self.qtile, self.index, x, y, w, h, self.group)
        for bar in [self.top, self.bottom, self.left, self.right]:
            if bar:
                bar.draw()
        self.qtile.call_soon(self.group.layout_all)

    def cmd_info(self):
        """Returns a dictionary of info for this screen."""
        return dict(
            index=self.index,
            width=self.width,
            height=self.height,
            x=self.x,
            y=self.y
        )

    def cmd_resize(self, x=None, y=None, w=None, h=None):
        """Resize the screen"""
        self.resize(x, y, w, h)

    def cmd_next_group(self, skip_empty=False, skip_managed=False):
        """Switch to the next group"""
        n = self.group.get_next_group(skip_empty, skip_managed)
        self.set_group(n)
        return n.name

    def cmd_prev_group(self, skip_empty=False, skip_managed=False, warp=True):
        """Switch to the previous group"""
        n = self.group.get_previous_group(skip_empty, skip_managed)
        self.set_group(n, warp=warp)
        return n.name

    def cmd_toggle_group(self, group_name=None, warp=True):
        """Switch to the selected group or to the previously active one"""
        group = self.qtile.groups_map.get(group_name)
        self.toggle_group(group, warp=warp)


class Group:
    """Represents a "dynamic" group

    These groups can spawn apps, only allow certain Matched windows to be on
    them, hide when they're not in use, etc.
    Groups are identified by their name.

    Parameters
    ==========
    name: string
        the name of this group
    matches: default ``None``
        list of ``Match`` objects whose  windows will be assigned to this group
    exclusive: boolean
        when other apps are started in this group, should we allow them here or not?
    spawn: string or list of strings
        this will be ``exec()`` d when the group is created, you can pass
        either a program name or a list of programs to ``exec()``
    layout: string
        the name of default layout for this group (e.g. 'max' or 'stack').
        This is the name specified for a particular layout in config.py
        or if not defined it defaults in general the class name in all lower case.
    layouts: list
        the group layouts list overriding global layouts.
        Use this to define a separate list of layouts for this particular group.
    persist: boolean
        should this group stay alive with no member windows?
    init: boolean
        is this group alive when qtile starts?
    position  int
        group position
    label: string
        the display name of the group.
        Use this to define a display name other than name of the group.
        If set to None, the display name is set to the name.
    """
    def __init__(self, name: str, matches: List[Match] = None, exclusive=False,
                 spawn: Union[str, List[str]] = None, layout: str = None,
                 layouts: List = None, persist=True, init=True,
                 layout_opts=None, screen_affinity=None, position=sys.maxsize,
                 label: Optional[str] = None):
        self.name = name
        self.label = label
        self.exclusive = exclusive
        self.spawn = spawn
        self.layout = layout
        self.layouts = layouts or []
        self.persist = persist
        self.init = init
        self.matches = matches or []
        self.layout_opts = layout_opts or {}

        self.screen_affinity = screen_affinity
        self.position = position

    def __repr__(self):
        attrs = utils.describe_attributes(
            self,
            ['exclusive', 'spawn', 'layout', 'layouts', 'persist', 'init',
             'matches', 'layout_opts', 'screen_affinity'])
        return '<config.Group %r (%s)>' % (self.name, attrs)


class Match:
    """Match for dynamic groups or auto-floating windows.

    It can match by title, wm_class, role, wm_type, wm_instance_class or
    net_wm_pid.

    ``Match`` supports both regular expression objects (i.e. the result of
    ``re.compile()``) or strings (match as an "include"-match). If a window
    matches all specified values, it is considered a match.

    Parameters
    ==========
    title:
        matches against the WM_NAME atom (X11) or title (Wayland)
    wm_class:
        matches against the second string in WM_CLASS atom (X11) or app ID (Wayland)
    role:
        matches against the WM_ROLE atom (X11 only)
    wm_type:
        matches against the WM_TYPE atom (X11 only)
    wm_instance_class:
        matches against the first string in WM_CLASS atom (X11) or app ID (Wayland)
    net_wm_pid:
        matches against the _NET_WM_PID atom (X11) or PID (Wayland) -
        (only int allowed for this rule)
    func:
        delegate the match to the given function, which receives the tested
        client as argument and must return True if it matches, False otherwise
    """
    def __init__(self, title=None, wm_class=None, role=None, wm_type=None,
                 wm_instance_class=None, net_wm_pid=None,
                 func: Callable[[base.WindowType], bool] = None):
        self._rules = {}

        if title is not None:
            self._rules["title"] = title
        if wm_class is not None:
            self._rules["wm_class"] = wm_class
        if wm_instance_class is not None:
            self._rules["wm_instance_class"] = wm_instance_class
        if net_wm_pid is not None:
            try:
                self._rules["net_wm_pid"] = int(net_wm_pid)
            except ValueError:
                error = 'Invalid rule for net_wm_pid: "%s" only int allowed' % \
                        str(net_wm_pid)
                raise utils.QtileError(error)
        if func is not None:
            self._rules["func"] = func

        if role is not None:
            self._rules["role"] = role
        if wm_type is not None:
            self._rules["wm_type"] = wm_type

    @staticmethod
    def _get_property_predicate(name, value):
        if name == 'net_wm_pid':
            return lambda other: other == value
        elif name == 'wm_class':
            def predicate(other):
                # match as an "include"-match on any of the received classes
                match = getattr(other, 'match', lambda v: v in other)
                return value and any(match(v) for v in value)
            return predicate
        else:
            def predicate(other):
                # match as an "include"-match
                match = getattr(other, 'match', lambda v: v in other)
                return match(value)
            return predicate

    def compare(self, client):
        for property_name, rule_value in self._rules.items():
            if property_name == 'title':
                value = client.name
            elif "class" in property_name:
                wm_class = client.get_wm_class()
                if not wm_class:
                    return False
                if property_name == "wm_instance_class":
                    value = wm_class[0]
                else:
                    value = wm_class
            elif property_name == 'role':
                value = client.get_wm_role()
            elif property_name == 'func':
                return rule_value(client)
            elif property_name == 'net_wm_pid':
                value = client.get_pid()
            else:
                value = client.get_wm_type()

            # Some of the window.get_...() functions can return None
            if value is None:
                return False

            match = self._get_property_predicate(property_name, value)
            if not match(rule_value):
                return False

        if not self._rules:
            return False
        return True

    def map(self, callback, clients):
        """Apply callback to each client that matches this Match"""
        for c in clients:
            if self.compare(c):
                callback(c)

    def __repr__(self):
        return '<Match %s>' % self._rules
