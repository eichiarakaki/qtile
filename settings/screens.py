from libqtile.config import Screen
from libqtile import bar
from libqtile.log_utils import logger
from settings.widgets import primary_widgets_barA, primary_widgets_barB, secondary_widgets
import subprocess


def bars():
    return [
        bar.Bar(primary_widgets_barA, 34, opacity=1, margin=[13, 25*31, 10, 25*31]),
        bar.Bar(primary_widgets_barB, 34, opacity=1, margin=[10, 100*1, 13, 100*1])
    ]


screens = [Screen(*bars())]


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
        screens.append(Screen(top=status_bar(secondary_widgets)))
