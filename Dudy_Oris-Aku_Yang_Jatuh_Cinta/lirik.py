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
        ("Aku", 0.32),
        ("Yang jatuh cinta", 0.11),
        ("Haruslah kau kuberi kesempatan", 0.07),
        ("Ingin aku jadi kekasih yang baik", 0.10),
        ("Berikan aku kesempatan", 0.09),
        ("Oh...", 0.09),
        ("Tahukah dirimu?", 0.06),
        ("Tahukah hatimu?", 0.06),
        ("Berulah keketuk, aku mencintaimu", 0.09),
        ("Tapi dirimu tak pernah sadari", 0.07),
        ("Aku", 0.27),
        ("Yang jatuh cinta", 0.10),
    ]
    delays = [3.5, 2, 2.6, 1.4, 2, 2.8, 2.4, 1.6, 2.1, 2.6, 3.5, 2]
    
    for i, (line, char_delay) in enumerate(lines):
        color = colors[i % len(colors)]
        for char in line:
            print(color + char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print(Style.RESET_ALL)  # Reset to default style after each line

def print_table():
    init(autoreset=True)
    table_title = "EVI CANDINI 💗"
    border = f"{Fore.YELLOW}{'=' * (len(table_title) + 4)}{Style.RESET_ALL}"
    
    print(Fore.YELLOW + border)
    print(Fore.YELLOW + f"| {Fore.RED}{table_title}{Fore.YELLOW} |")
    print(Fore.YELLOW + border + Style.RESET_ALL)

if __name__ == "__main__":
    file_path = "/root/perkuliahan/goodTimes/Dudy-Oris_Aku-Yang-Jatuh-Cinta/ajc.mp3"
    
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
