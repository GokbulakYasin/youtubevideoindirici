import yt_dlp
import os
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import askdirectory
import threading

# Videonun kaydedildiği klasör
DEFAULT_DOWNLOAD_FOLDER = os.path.join(os.getcwd(), 'downloads')

# Klasör yoksa oluşturuluyo
if not os.path.exists(DEFAULT_DOWNLOAD_FOLDER):
    os.makedirs(DEFAULT_DOWNLOAD_FOLDER)

# İndirilen dosya konumunu kullanıcı seçebilir
download_path = DEFAULT_DOWNLOAD_FOLDER

# İndirmenin çalıştığı arka plan thread'i
def download_video():
    link = entry_link.get()
    if not link:
        messagebox.showerror("Hata", "Lütfen geçerli bir video linki girin!")
        return

    # Kalite seçimi
    quality = combo_quality.get()
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'progress_hooks': [my_hook],
    }

    if quality == "720p":
        ydl_opts['format'] = 'bestvideo[height<=720]+bestaudio/best'
    elif quality == "480p":
        ydl_opts['format'] = 'bestvideo[height<=480]+bestaudio/best'
    elif quality == "MP3":
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'progress_hooks': [my_hook],
        }

    # YDL ile video indirme
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([link])
        except Exception as e:
            messagebox.showerror("Hata", f"Video indirilirken bir hata oluştu: {e}")
            return
    messagebox.showinfo("İşlem Tamamlandı", "Video başarıyla indirildi!")

# Progress bar'ı güncelleyen hook fonksiyonu
def my_hook(d):
    if d['status'] == 'downloading':
        percent = d['downloaded_bytes'] / d['total_bytes'] * 100
        progress_var.set(percent)
    elif d['status'] == 'finished':
        progress_var.set(100)

# Klasör seçme fonksiyonu
def select_folder():
    global download_path
    folder = askdirectory(title="İndirme Klasörü Seçin")
    if folder:
        download_path = folder
        label_folder.config(text=f"İndirilenler: {download_path}")

# GUI penceresini oluştur
root = tk.Tk()
root.title("YouTube Video İndirici")

# Pencere boyutlandırma
root.geometry("400x350")
root.resizable(False, False)

# Başlık etiketi
label_title = tk.Label(root, text="YouTube Video İndirici", font=("Arial", 16), pady=10)
label_title.pack()

# Video linki girişi
label_link = tk.Label(root, text="Video Linki:")
label_link.pack(pady=5)
entry_link = tk.Entry(root, width=40)
entry_link.pack(pady=5)

# Kalite seçimi
label_quality = tk.Label(root, text="İndirme Kalitesi:")
label_quality.pack(pady=5)
combo_quality = ttk.Combobox(root, values=["En iyi kalite", "720p", "480p", "MP3"], state="readonly", width=40)
combo_quality.set("En iyi kalite")  # Varsayılan olarak "En iyi kalite"
combo_quality.pack(pady=5)

# İndirilen dosya konumu etiketi ve klasör seçme butonu
label_folder = tk.Label(root, text=f"İndirilenler: {download_path}", wraplength=300)
label_folder.pack(pady=5)
btn_folder = tk.Button(root, text="Klasör Seç", command=select_folder)
btn_folder.pack(pady=5)

# İndirme işlemi için progress bar
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100, length=300)
progress_bar.pack(pady=15)

# İndirme başlatma butonu
btn_download = tk.Button(root, text="İndirmeyi Başlat", command=lambda: threading.Thread(target=download_video).start())
btn_download.pack(pady=10)

# Pencereyi başlat
root.mainloop()

#Hazırlayan Yasin Gökbulak