import subprocess
from typing import Dict, List, Tuple

# workspace num / (Occupied, Focused)
workspaces: Dict[int, Tuple[bool, bool]] = {}

def names_filter(v: str) -> str:
    for i in v:
        if  i.isdigit() == True and len(v) == 3 and '\n' in v:
            return v.split('\n')[0]


def ws_focused(v: List) -> str:
    v = list(filter(lambda x: x != '', v))
    return list(v[v.index('*') - 1])[0]


def ws_occupied(v: List) -> List[str]:
    pass


def main():
    wml = subprocess.run("wmctrl -l", 
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    wmd = subprocess.run("wmctrl -d", 
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # workspaces name
    ws_names = wmd.stdout.decode("utf-8").split(' ')
    ws_names = [names_filter(i) for i in  ws_names if names_filter(i) != None]

    # check if focused
    ws_focused_n = wmd.stdout.decode("utf-8").split(' ')
    ws_focused_n = ws_focused(ws_focused_n)

    # check if Occupied
    ws_occupied_ns = wmd.stdout.decode("utf").split(' ')


if __name__ == '__main__':
    main()