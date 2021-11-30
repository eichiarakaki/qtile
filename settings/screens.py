from typing import Optional
from libqtile.bar import (
    Gap, 
    BarType, 
    Bar,
)
from custom.config import Screen

from settings import mkbar
from settings.widgets import bar_widgets, secondary_widgets
import subprocess
from libqtile.log_utils import logger

def main_bar() -> Optional[BarType]:
    bar = mkbar.NewBar()
    bar.widget(bar_widgets) # widgets
    bar.opacity(1.0) # opacity
    bar.geometry(1780, 45) # width / height
    bar.positions(100, 22) # X / Y
    bar.margin(20)

    return bar.assembler()

def status_bar(widgets):
    return Bar(widgets, 24, opacity=0.92)

screens = [Screen(
            top = Gap(15),#Gap(70),
            bottom = Gap(15),
            left = Gap(15),
            right = Gap(15),
        )]
screens.clear() 
"""
xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if command.returncode != 0:
    error = command.stderr.decode("UTF-8")
    logger.error(f"Failed counting monitors using {xrandr}:\n{error}")
    connected_monitors = 1
else:
    connected_monitors = int(command.stdout.decode("UTF-8"))

if connected_monitors > 1:
    for _ in range(1, connected_monitors):
        screens.append(Screen(top=Gap(15), bottom=Gap(15), left=Gap(15), right=Gap(15)))
"""