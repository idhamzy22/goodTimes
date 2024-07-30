import pygame
from time import sleep
import time
import sys
import os
from colorama import init, Fore, Style

def print_lirik():
    init(autoreset=True)
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    
    lines = [
        ("......", 0.09),
        ("WHERE WE ARE AND LET GO", 0.12),
        ("WE'RE SO CLOSE", 0.07),
        ("IF YOU DON'T KNOW", 0.05),
        ("WHERE TO START", 0.13),
        ("JUST HOLD ON", 0.09),
        ("AND DON'T RUN", 0.09),
        ("WE'RE LOOKING BACK", 0.04),
        ("WE'RE MESSING AROUND?", 0.03),
        ("BUT THAT WAS THEN", 0.04),
        ("AND THIS IS NOW", 0.05),
        ("ALL WE NEED IS ENOUGH LOVE", 0.09),
        ("TO HOLD US", 0.10),
        ("WHERE WE ARE", 0.10),
    ]
    delays = [0.9, 0.8, 1, 0.09, 0.13, 1, 2.5, 1.2, 1.5, 1, 0.09, 1.4, 1.1, 1]
    
    for i, (line, char_delay) in enumerate(lines):
        color = colors[i % len(colors)]
        for char in line:
            print(color + char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print(Style.RESET_ALL)

def print_table():
    init(autoreset=True)
    table_title = "IDHAMZYY 👾"
    border = f"{Fore.YELLOW}{'=' * (len(table_title) + 5)}{Style.RESET_ALL}"
    
    print(Fore.YELLOW + border)
    print(Fore.YELLOW + f"| {Fore.RED}{table_title}{Fore.YELLOW} |")
    print(Fore.YELLOW + border + Style.RESET_ALL)

if __name__ == "__main__":
    file_path = "/root/perkuliahan/goodTimes/one-direction/ow.mp3"
    
    if not os.path.exists(file_path):
        print(f"File tidak ditemukan: {file_path}")
        sys.exit(1)
    
    # Print the table before playing the song
    print_table()
    
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    
    print_lirik()
    
    while pygame.mixer.music.get_busy():
        time.sleep(1)
