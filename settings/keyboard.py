from subprocess import (
      run
    , PIPE
)
from settings.notify import Notify


class KeyboardLayout:
    def __init__(self, kbs: list) -> None:
        self.kbs: list = kbs
        self._next_kb: str = ''
    
    
    def which_kb(self) -> str:
        notification = Notify()
        try:
            kb = run("setxkbmap -query | grep layout | awk '{ print $2 }'", shell=True, stdout=PIPE, stderr=PIPE)
            return kb.stdout.decode('UTF-8').replace('\n', '')
        except:
            notification.set_title('Keyboard layouts')
            notification.set_summary('Couldn\'t get current keyboard layout.')
            notification.show()
    
    
    def next_kb(self) -> None:
        ckb = self.which_kb()
        idx = self.kbs.index(ckb)
        notification = Notify()


        try:
            self._next_kb = self.kbs[idx + 1]
        except:
            self._next_kb = self.kbs[0]
        
        setting_kb = run(
            'setxkbmap %s' % self._next_kb,
            shell=True,
            stdout=PIPE,
            stderr=PIPE,
        )

        if setting_kb.returncode != 0:
            notification.set_title('Keyboard layouts')
            notification.set_summary('Failed to switch next layout.')
            notification.show()
        else:
            notification.set_title('Keyboard layouts')
            notification.set_summary('Switched to %s.' % self._next_kb.upper())
            notification.set_timeout(3)
            notification.show()



def next_layout(qtile, kbs: list):
    aux = KeyboardLayout(kbs)
    aux.next_kb()
