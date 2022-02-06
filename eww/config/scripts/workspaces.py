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

print('names:', ws_names)
print('focused:', int(ws_focused_n) + 1)
print('ws_occupied:', ws_occupied_ns)

for i, (n, k, v) in ws.items():
    print(i, n, k, v)


# print(f'(box	:class \"works\" :orientation \"v\"	:halign \"center\"	:valign \"start\"	 :space-evenly \"false\" :spacing \"-5\" (button :onclick \"wmctrl -s 0\"	:class	\"0{ws.get(1)[1]}{ws.get(1)[2]}\"	\"\") (button :onclick \"bspc desktop -f $ws2\"	:class \"$un$o2$f2\"	 \"\") (button :onclick \"bspc desktop -f $ws3\"	:class \"$un$o3$f3\" \"\") (button :onclick \"bspc desktop -f $ws4\"	:class \"$un$o4$f4\"	\"\") (button :onclick \"bspc desktop -f $ws5\"	:class \"$un$o5$f5\" \"\" )  (button :onclick \"bspc desktop -f $ws6\"	:class \"$un$o6$f6\" \"\") (button :onclick \"bspc desktop -f $ws7\"	:class \"$un$o7$f7\" \"\") (button :onclick \"bspc desktop -f $ws8\"	:class \"$un$o8$f8\" \"\") (button :onclick \"bspc desktop -f $ws9\"	:class \"$un$o9$f9\" \"\"))')
