import subprocess
from libqtile.config import Screen
from libqtile.bar import (
    Gap, 
    BarType, 
    # Bar,
)
from libqtile.log_utils import logger
from typing import Optional
from settings import mkbar
"""Most recently made configuration
from settings.widgets import bar_widgets
"""

def main_bar() -> Optional[BarType]:
    bar = mkbar.NewBar()
    # bar.widget(bar_widgets) # widgets
    bar.opacity(1.0) # opacity
    bar.geometry(600, 45) # width / height
    bar.positions(690, 10) # X / Y
    bar.margin(20)

    return bar.assembler()

"""
screens: list = [Screen(
            top = main_bar(),
            bottom = Gap(15),
            left = Gap(15),
            right = Gap(15),
        )]
"""
screens: list = []


xrandr = 'xrandr | grep -w "connected" | cut -d ' ' -f 2 | wc -l'
command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if command.returncode != 0:
    error = command.stderr.decode('UTF-8')
    logger.error('Failed counting monitors using %s:\n%s' % (xrandr, error))
    connected_monitors = 1
else:
    connected_monitors = int(command.stdout.decode('UTF-8'))

if connected_monitors > 1:
    for _ in range(1, connected_monitors):
        screens.append(Screen(
            top=Gap(5), 
            bottom=Gap(5), 
            left=Gap(5), 
            right=Gap(5),
        ))