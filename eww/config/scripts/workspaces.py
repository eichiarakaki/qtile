import subprocess
from typing import Dict, List, Tuple

# workspace num / (ws name, Occupied, Focused)
ws: Dict[int, Tuple[str, int, int]] = {}

def names_filter(v: str) -> int:
    for i in v:
        if  i.isdigit() == True and len(v) == 3 and '\n' in v:
            return v.split('\n')[0]
        if i.isdigit() != True and len(v) == 2 and '\n' in v:
            return v.split('\n')[0]


def ws_focused(v: List) -> int:
    v = list(filter(lambda x: x != '', v))
    return list(v[v.index('*') - 1])[2]


def ws_occupied(v: str) -> int:
    return int(v.split(' ')[2]) + 1


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
ws_names = [names_filter(v) for v in ws_names if names_filter(v) != None]

 # check if focused
ws_focused_n = wmd.stdout.decode("utf-8").split(' ')
ws_focused_n = ws_focused(ws_focused_n)
ws_focused_n = int(ws_focused_n) + 1

 # check if Occupied
ws_occupied_ns = wml.stdout.decode("utf-8").splitlines()
ws_occupied_ns = [ws_occupied(i) for i in ws_occupied_ns]
 # -------

# 1..9 if True else Blank
ws = {
    1: (ws_names[0], False if not 1 in ws_occupied_ns else True, True if ws_focused_n == 1 else False),
    2: (ws_names[1], False if not 2 in ws_occupied_ns else True, True if ws_focused_n == 2 else False),
    3: (ws_names[2], False if not 3 in ws_occupied_ns else True, True if ws_focused_n == 3 else False),
    4: (ws_names[3], False if not 4 in ws_occupied_ns else True, True if ws_focused_n == 4 else False),
    5: (ws_names[4], False if not 5 in ws_occupied_ns else True, True if ws_focused_n == 5 else False),
    6: (ws_names[5], False if not 6 in ws_occupied_ns else True, True if ws_focused_n == 6 else False),
    7: (ws_names[6], False if not 7 in ws_occupied_ns else True, True if ws_focused_n == 7 else False),
    8: (ws_names[7], False if not 8 in ws_occupied_ns else True, True if ws_focused_n == 8 else False),
    9: (ws_names[8], False if not 9 in ws_occupied_ns else True, True if ws_focused_n == 9 else False),
}


def no_falses(wss):
    if wss != True:
        return True
    else:
        return ''
'''
print('names:', ws_names)
print('focused:', int(ws_focused_n) + 1)
print('ws_occupied:', ws_occupied_ns)

for i, (n, k, v) in ws.items():
    print(i, n, k, v)
'''

print('(box	:class \"works\" :orientation \"v\"	:halign \"center\"	:valign \"start\"	 :space-evenly \"false\" :spacing \"-5\" (button :onclick \"wmctrl -s 0\"	:class	\"0%s%s\"	\"%s\") (button :onclick \"wmctrl -s 1\"	:class \"0%s%s\"	 \"%s\") (button :onclick \"wmctrl -s 2\"	:class \"0%s%s\" \"%s\") (button :onclick \"wmctrl -s 3\"	:class \"0%s%s\"	\"%s\") (button :onclick \"wmctrl -s 4\"	:class \"0%s%s\" \"%s\" )  (button :onclick \"wmctrl -s 5\"	:class \"0%s%s\" \"%s\") (button :onclick \"wmctrl -s 6\"	:class \"0%s%s\" \"%s\") (button :onclick \"wmctrl -s 7\"	:class \"0%s%s\" \"%s\") (button :onclick \"wmctrl -s 8\"	:class \"0%s%s\" \"%s\"))'
% (
    1 if ws.get(1)[1] == True else '',
    1 if ws.get(1)[2] == True else '',
    ws.get(1)[0],
    
    2 if ws.get(2)[1] == True else '',
    2 if ws.get(2)[2] == True else '',
    ws.get(2)[0],
    
    3 if ws.get(3)[1] == True else '',
    3 if ws.get(3)[2] == True else '',
    ws.get(3)[0],
    
    4 if ws.get(4)[1] == True else '',
    4 if ws.get(4)[2] == True else '',
    ws.get(4)[0],
    
    5 if ws.get(5)[1] == True else '',
    5 if ws.get(5)[2] == True else '',
    ws.get(5)[0],
    
    6 if ws.get(6)[1] == True else '',
    6 if ws.get(6)[2] == True else '',
    ws.get(6)[0],
    
    7 if ws.get(7)[1] == True else '',
    7 if ws.get(7)[2] == True else '',
    ws.get(7)[0],
    
    8 if ws.get(8)[1] == True else '',
    8 if ws.get(8)[2] == True else '',
    ws.get(8)[0],
    
    9 if ws.get(9)[1] == True else '',
    9 if ws.get(9)[2] == True else '',
    ws.get(9)[0],
    
    ))
