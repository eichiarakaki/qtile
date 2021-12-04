from datetime import datetime
from os.path import join
from path import dunst_path 
from subprocess import PIPE, run, getoutput

def jp_format():
    now = datetime.now()

    month = now.strftime('%m')
    day = now.strftime("%d")
    weekday = now.strftime('%A')
    hour = now.strftime("%H")
    minute = now.strftime("%M")

    months = {
        '1': '一月',
        '2': 'ニ月',
        '3': '三月',
        '4': '四月',
        '5': '五月',
        '6': '六月',
        '7': '七月',
        '8': '八月',
        '9': '九月',
        '10': '十月',
        '11': '十一月',
        '12': '十二月',
    }
    weekdays = {
        'Sunday':  '日曜日',
        'Monday':  '月曜日',
        'Tuesday': '火曜日',
        'Wednesday': '水曜日',
        'Thursday': '木曜日',
        'Friday': '金曜日',
        'Saturday': '土曜日',
    }

    return months[month], weekdays[weekday], day, hour, minute


# def large_format():
#    month, weekday, day, hour, minute = jp_format()
#    return print('%s %s%s - %s:%s' % (month, day, weekday, hour, minute), end='')

def short_format():
    _, _, day, hour, minute = jp_format()
    notify_format: str = 'dunstify "Date" "%s日 - %s:%s" -t 5000 -I %s' % (day, hour, minute, join(dunst_path, 'SettingsBlue.png'))

    run(
        notify_format,
        shell=True,
        stdout=PIPE,
        stderr=PIPE
    )


def workspace_notify():
    """ Needs wmctrl """
    cmd: str = getoutput("wmctrl -d").split('\n')  
    wk = list(filter(lambda x: '*' in x, cmd))[0][0]
    
    notify_format: str = 'dunstify "Workspaces" "Switched to workspace %s" -t 1500 -I %s' % (int(wk) + 1, join(dunst_path, 'SettingsBlue.png'))

    run(
        notify_format,
        shell=True,
        stdout=PIPE,
        stderr=PIPE
    )

short_format()
workspace_notify()