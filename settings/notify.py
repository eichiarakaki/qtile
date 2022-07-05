import subprocess
import enum


class Urgency(enum.Enum):
    low:        int = 1
    normal:     int = 2
    critical:   int = 3



class Notify:
    def __init__(self) -> None:
        self.urgency: Urgency = Urgency(2)
        self.icon:    str     = None
        self.timeout: int     = 5000
        self.title:   str
        self.summary: str


    def set_title(self, title: str) -> None:
        self.title = title

    def set_summary(self, summary: str) -> None:
        self.summary = summary

    def set_urgency(self, level: int = 2) -> None:
        self.urgency = Urgency(level)

    def set_icon(self, icon: str) -> None:
        self.icon = icon

    def set_timeout(self, seconds: int) -> int:
        self.timeout = seconds * 1000


    def show(self) -> None:
        subprocess.run('%s %s %s %s %s %s' % (
             'notify-send' 
            , '"'   + self.title + '"'
            , '"'   + self.summary + '"'
            , '-u ' + self.urgency.name
            , '-t ' + str(self.timeout) if self.timeout != None else ''
            , '-i ' + self.icon if self.icon != None else ''

        ), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
