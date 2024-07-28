# Menampilkan Lirik dengan Pemutaran MP3

Proyek ini adalah program Python yang memutar file MP3 sambil menampilkan lirik di konsol. Lirik muncul karakter demi karakter dan baris demi baris, dengan setiap baris diberi warna yang berbeda.

## Prasyarat

- Python 3.x
- Pustaka `pygame`
- Pustaka `colorama`

## Instalasi

1. Instal pustaka yang diperlukan dengan menjalankan perintah berikut di terminal:
    ```bash
    pip install pygame colorama
    ```

2. Pastikan Anda memiliki file MP3 di jalur yang ditentukan. Pada contoh ini, jalur file MP3 adalah:
    ```plaintext
    /linux/ubuntu/root/perkuliahan/goodTimes/Dudy-Oris_Aku-Yang-Jatuh-Cinta/ajc.mp3
    ```
   Anda dapat mengganti jalur ini dengan lokasi file MP3 yang Anda miliki.

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

## Penjelasan Fungsi

1. **print_lirik()**
    - Fungsi ini bertanggung jawab untuk menampilkan lirik lagu dengan efek warna.
    - Inisialisasi `colorama` dengan `init(autoreset=True)` untuk otomatis mengatur ulang warna setelah setiap karakter.
    - Mendefinisikan daftar warna yang akan digunakan untuk setiap baris lirik.
    - Menyusun lirik lagu dalam bentuk daftar tuple, di mana setiap tuple berisi baris lirik dan penundaan antara setiap karakter.
    - Daftar `delays` berisi waktu tunggu antar baris.
    - Loop utama iterasi melalui setiap baris, mengatur warna berdasarkan indeks, dan mencetak setiap karakter dengan penundaan yang ditentukan.
    - Setelah mencetak satu baris lengkap, program akan menunggu sesuai waktu dalam daftar `delays` sebelum melanjutkan ke baris berikutnya.
    - `print(Style.RESET_ALL)` mengatur ulang gaya teks ke default setelah setiap baris dicetak.

2. **print_table()**
    - Fungsi ini bertugas untuk mencetak tabel dengan judul yang ditampilkan dalam warna yang berbeda.
    - Inisialisasi `colorama` dengan `init(autoreset=True)` untuk mengatur ulang warna secara otomatis setelah digunakan.
    - Judul tabel disimpan dalam variabel `table_title`.
    - Variabel `border` berisi baris tanda sama dengan yang panjangnya sesuai dengan panjang judul tabel.
    - Mencetak batas atas, judul dengan warna yang berbeda, dan batas bawah tabel.

3. **Blok Eksekusi Utama**
    - Bagian ini adalah titik masuk utama dari program.
    - Memeriksa apakah file MP3 yang ditentukan ada di jalur yang ditentukan. Jika tidak, mencetak pesan kesalahan dan keluar dari program.
    - Jika file ada, mencetak tabel dengan memanggil `print_table()`.
    - Inisialisasi mixer `pygame` dan memuat file MP3.
    - Memulai pemutaran musik dengan `pygame.mixer.music.play()`.
    - Memanggil fungsi `print_lirik()` untuk menampilkan lirik lagu yang sinkron dengan pemutaran musik.
    - Loop `while pygame.mixer.music.get_busy()` memastikan program tetap berjalan selama musik masih diputar.

## Catatan

- Pastikan jalur file MP3 sudah benar. Jika file MP3 berada di lokasi yang berbeda, ubah variabel `file_path` sesuai dengan jalur yang benar.
- Anda mungkin perlu menyesuaikan nilai penundaan dalam daftar `lines` dan `delays` agar lirik lebih sinkron dengan musik yang diputar.
- Program ini akan mencetak pesan kesalahan dan keluar jika file MP3 tidak ditemukan di lokasi yang ditentukan.
