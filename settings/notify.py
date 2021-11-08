
# This module needs improvement.
# Need to handle the erreros.

import sys
import os
sys.path.append('{}/.config/qtile/settings'.format(os.getcwd()))
from path import qtile_path

from pathlib import Path
import subprocess
from enum import Enum

global second
global ICON_PATH
second = 1000
icon_path = Path(f'{qtile_path}/icons')

class __NotifyError(Exception):
    pass


def __notify_icon(ico: str) -> Path:
    class __Notify_icon(Enum):
        calendar: Path = '{}/Calendar.png'.format(icon_path)
        clock:    Path = '{}/Clock.png'.format(icon_path)
        error:    Path = '{}/Error.png'.format(icon_path)
        heart:    Path = '{}/Heart.png'.format(icon_path)
        settings: Path = '{}/Settings.png'.format(icon_path)

        def __str__(self) -> Path:
            return self.value

    if ico.lower() == 'calendar':
        return __Notify_icon.calendar
    elif ico.lower() == 'clock':
        return __Notify_icon.clock
    elif ico.lower() == 'error':
        return __Notify_icon.error
    elif ico.lower() == 'heart':
        return __Notify_icon.heart
    else:
        return __Notify_icon.settings


def __urgency(level: str) -> str:
    class __urgency_level(Enum):
        prefix:   str = '--urgency='
        low:      str = '{}low'.format(prefix)
        normal:   str = '{}normal'.format(prefix)
        critical: str = '{}critical'.format(prefix)

        def __str__(self) -> str:
            return self.value


    if level.lower() == 'low':
        return __urgency_level.low
    elif level.lower() == 'normal':
        return __urgency_level.normal
    elif level.lower() == 'critical':
        return __urgency_level.critical
    else:
        return __urgency_level.normal


class __Notify:
    def __init__(self) -> None:
        pass

    def _send(self, urgency, main_text: str, secondary_text: str, 
               icon: str, expiration_time: int)-> None:

        notify_format : str = 'notify-send {} -i {} -t {} "{}" "{}"'.format(
            urgency, icon, expiration_time, main_text, secondary_text
        )

        subprocess.run(
            notify_format,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )



def send(main_text: str = '', secondary_text: str= '',
                icon: str = 'settings',
                urgency: str = 'normal',
                expiration_time: int = second*5):
        
    __Notify()._send(__urgency(urgency), 
                      main_text, secondary_text,
                      __notify_icon(icon), expiration_time*second)
