from os import system
from datetime import datetime
from settings.path import qtile_path, picom_path
import subprocess


def night(current_hour : int):
    if current_hour in range(17, 24) or current_hour in range(0,10):
        system('redshift -x')
        system('redshift -O 4000')
    if current_hour in range(19, 24) or current_hour in range(0,12): 
        system('brightnessctl set 30%')

def day(current_hour : int):
    if current_hour in range(13, 16): system('redshift -x')
    if current_hour in range(11, 18): system('brightnessctl set 80%')

def run():
    system(f'~/bin/eww daemon')
   # cmd = subprocess.Popen(f'~/bin/eww daemon', stdout=subprocess.PIPE, shell=True)
   # output, err = cmd.communicate()
   # p_status = cmd.wait()
    system(f'picom &')
    system(f'udiskie &')
    system(f'~/.fehbg &')
    system(f'dunst &')
    system(f'playerctld daemon &')
    #system(f'bash {qtile_path}/scripts/feh-blur &')
    
if __name__ == '__main__':
    current_hour : int = int(datetime.now().strftime("%H"))
    night(current_hour)
    day(current_hour)
    run()
    
