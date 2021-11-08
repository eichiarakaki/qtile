import subprocess
import datetime


def jp_format():
    now = datetime.datetime.now()

    month = now.strftime('%m')
    day = now.strftime("%d日")
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
    notify_format : str = 'notify-send "Time" "%s - %s:%s" -t 5000' % (day, hour, minute)

    subprocess.run(
        notify_format,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )


def workspace_notify():
    """ Needs wmctrl """
    cmd: str = subprocess.getoutput("wmctrl -d").split('\n')  
    wk = list(filter(lambda x: '*' in x, cmd))[0][0]
    
    notify_format : str = 'notify-send "Workspaces" "You are currently in workspace %s" -t 1500' % (int(wk) + 1)

    subprocess.run(
        notify_format,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

short_format()
workspace_notify()