import os


class Game_settings:
    def check_os():
        os.system('cls' if os.name == 'nt' else 'clear')
