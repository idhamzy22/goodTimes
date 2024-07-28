# Menampilkan Lirik dengan Pemutaran MP3

Proyek ini adalah program Python yang memutar file MP3 sambil menampilkan lirik di konsol. Lirik muncul karakter demi karakter dan baris demi baris, dengan setiap baris diberi warna yang berbeda.

## Prasyarat

- Python 3.x
- Pustaka `pygame`
- Pustaka `colorama`

## Instalasi

1. Instal pustaka yang diperlukan:
    ```bash
    pip install pygame colorama
    ```

2. Pastikan Anda memiliki file MP3 di jalur yang ditentukan:
    ```plaintext
    /root/perkuliahan/goodTimes/Dudy-Oris_Aku-Yang-Jatuh-Cinta/ajc.mp3
    ```

## Penggunaan

1. Simpan kode berikut dalam file bernama `lirik.py`:

    ```python
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
            print(Style.RESET_ALL)  # Reset ke gaya default setelah setiap baris

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
        
        # Cetak tabel sebelum memutar lagu
        print_table()
        
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        
        print_lirik()
        
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    ```

2. Jalankan skrip:
    ```bash
    python lirik.py
    ```

## Fungsi

1. **print_lirik()**
    - Fungsi ini menginisialisasi `colorama` dan mendefinisikan warna untuk lirik.
    - Mendefinisikan baris lirik dan penundaan antara setiap karakter dan setiap baris.
    - Mengiterasi setiap baris dan mencetaknya karakter demi karakter dengan penundaan dan warna yang ditentukan.
    - Setelah mencetak setiap baris, menunggu penundaan yang ditentukan sebelum mencetak baris berikutnya.

2. **print_table()**
    - Fungsi ini mencetak tabel dengan judul menggunakan `colorama` untuk teks berwarna.
    - Menginisialisasi `colorama` dan mencetak judul yang dibatasi oleh garis tanda sama dengan.

3. **Blok Eksekusi Utama**
    - Memeriksa apakah file MP3 yang ditentukan ada.
    - Jika file ada, mencetak tabel dan mulai memutar file MP3 menggunakan `pygame`.
    - Memanggil fungsi `print_lirik()` untuk menampilkan lirik yang sinkron dengan lagu.
    - Menjaga skrip tetap berjalan hingga file MP3 selesai diputar.

## Catatan

- Pastikan jalur file MP3 sudah benar.
- Sesuaikan penundaan dan lirik sesuai kebutuhan agar sinkron sempurna dengan lagu.
