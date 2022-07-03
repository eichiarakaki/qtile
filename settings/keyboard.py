from libqtile.command import lazy
from os import system
from subprocess import (
      run
    , PIPE
)

class KeyboardLayout:
    def __init__(self, kbs: list) -> None:
        self.kbs: list = kbs
        self._next_kb: str = ''
    
    
    def which_kb(self) -> str:
        try:
            kb = run("setxkbmap -query | grep layout | awk '{ print $2 }'", shell=True, stdout=PIPE, stderr=PIPE)
            return kb.stdout.decode('UTF-8').replace('\n', '')
        except:
            raise Exception('Couldn\'t get current keyboard layout.')
        finally:
            # notify user
            pass
    
    
    def next_kb(self) -> None:
        ckb = self.which_kb()
        idx = self.kbs.index(ckb)
        
        try:
            self._next_kb = self.kbs[idx + 1]
        except:
            self._next_kb = self.kbs[0]
        
        system('setxkbmap %s' % self._next_kb)
        


def next_layout(qtile, kbs: list):
    aux = KeyboardLayout(kbs)
    aux.next_kb()
