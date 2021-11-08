from datetime import date, datetime
import subprocess
from os import path
import webbrowser
from settings.notify import send as notify_send

global HOME
HOME = path.expanduser("~")


class TimeDate():
    def __init__(self) -> None:
        self.today : date = date.today()
        self.time : datetime = datetime.now()


    def show_date(self) -> None:
        format_date : str = self.today.strftime("%A, %b %d - %Y")
        notify_send('Current Date', format_date, icon='Calendar')


    def show_time(self) -> None:
        format_time : str = self.time.strftime("%H:%M")
        notify_send('Current Date', format_time, icon='Clock')


class Rofi:
    def __init__(self) -> None:
        self.home = HOME

    def powermenu(self):
        return f'{self.home}/.config/rofi/powermenu/powermenu.sh'


class Web:
    def __init__(self) -> None:
        self.github_url   = 'https://github.com/'
        self.chrome_url   = 'https://www.google.com/'
        self.reddit_url   = 'https://www.reddit.com/'
        self.youtube_url  = 'https://www.youtube.com/'

    def open_github(self) -> None:
        webbrowser.open_new(self.github_url)
    
    def open_chrome(self) -> None:
        webbrowser.open_new_tab(self.chrome_url)

    def open_reddit(self) -> None:
        webbrowser.open_new(self.reddit_url)
    
    def open_youtube(self) -> None:
        webbrowser.open_new(self.youtube_url)


class Programs:
    def __init__(self) -> None:
        self.home = HOME
        self.spotify_cmd = 'spotify &'


    def open_spotify(self) -> str:
        return self.spotify_cmd


    def get_player_status(self) -> str:
        current_playerctl = subprocess.run(
            ["bash", f"{self.home}/.config/qtile/scripts/getplayerstatus.sh"], 
            capture_output=True
            ).stdout

        return current_playerctl.decode()


    def get_player_title(self) -> str:
        current_playerctl = subprocess.run(
            ["bash", f"{self.home}/.config/qtile/scripts/getplayerformatted.sh"], 
            capture_output=True
            ).stdout

        return current_playerctl.decode()


    def pause_play_playerctl(self) -> None:
            command = f"bash {self.home}/.config/qtile/scripts/pause_play_playerctl.sh"
            subprocess.run(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

    def playerctl_next(self) -> None:
            command = f"bash {self.home}/.config/qtile/scripts/playerctl_next.sh"
            subprocess.run(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

    def playerctl_previous(self) -> None:
            command = f"bash {self.home}/.config/qtile/scripts/playerctl_previous.sh"
            subprocess.run(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
    
    def battery(self) -> str:
        current_playerctl = subprocess.run(
            ["bash", f"{self.home}/.config/qtile/scripts/battery.sh"], 
            capture_output=True
            ).stdout

        return current_playerctl.decode()